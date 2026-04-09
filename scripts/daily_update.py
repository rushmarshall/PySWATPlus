"""Daily synthetic benchmark for calibration algorithms.

Runs DDS, PSO, GLUE, and Sobol optimization on the Rosenbrock test function,
records convergence performance, and updates docs/ with results.
"""

import csv
import hashlib
import os
from datetime import datetime, timezone

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

DOCS_DIR = os.path.join(os.path.dirname(__file__), os.pardir, "docs")
BENCHMARK_MD = os.path.join(DOCS_DIR, "benchmarks.md")
CONVERGENCE_PNG = os.path.join(DOCS_DIR, "benchmark-convergence.png")
HISTORY_CSV = os.path.join(DOCS_DIR, "benchmark-history.csv")

SEED = int(datetime.now(timezone.utc).strftime("%Y%m%d"))
MAX_ITER = 500
BOUNDS = np.array([[-5.0, 5.0], [-5.0, 5.0]])


# ---------------------------------------------------------------------------
# Rosenbrock objective  f(x,y) = (1-x)^2 + 100*(y-x^2)^2
# ---------------------------------------------------------------------------

def rosenbrock(x: np.ndarray) -> float:
    return float((1 - x[0]) ** 2 + 100 * (x[1] - x[0] ** 2) ** 2)


# ---------------------------------------------------------------------------
# Optimisation algorithms
# ---------------------------------------------------------------------------

def _clip(x: np.ndarray) -> np.ndarray:
    return np.clip(x, BOUNDS[:, 0], BOUNDS[:, 1])


def dds(rng: np.random.Generator, max_iter: int = MAX_ITER) -> list[float]:
    """Dynamically Dimensioned Search."""
    dim = BOUNDS.shape[0]
    x_best = rng.uniform(BOUNDS[:, 0], BOUNDS[:, 1])
    f_best = rosenbrock(x_best)
    history = [f_best]

    for i in range(1, max_iter):
        prob = 1.0 - np.log(i) / np.log(max_iter)
        mask = rng.random(dim) < prob
        if not mask.any():
            mask[rng.integers(dim)] = True
        x_new = x_best.copy()
        sigma = 0.2 * (BOUNDS[:, 1] - BOUNDS[:, 0])
        x_new[mask] += rng.normal(0, sigma[mask])
        x_new = _clip(x_new)
        f_new = rosenbrock(x_new)
        if f_new < f_best:
            x_best, f_best = x_new, f_new
        history.append(f_best)
    return history


def pso(rng: np.random.Generator, max_iter: int = MAX_ITER,
        n_particles: int = 30) -> list[float]:
    """Particle Swarm Optimisation."""
    dim = BOUNDS.shape[0]
    pos = rng.uniform(BOUNDS[:, 0], BOUNDS[:, 1], (n_particles, dim))
    vel = rng.uniform(-1, 1, (n_particles, dim))
    pbest = pos.copy()
    pbest_f = np.array([rosenbrock(p) for p in pos])
    gbest_idx = pbest_f.argmin()
    gbest = pbest[gbest_idx].copy()
    gbest_f = pbest_f[gbest_idx]
    history = [gbest_f]

    w, c1, c2 = 0.7, 1.5, 1.5
    for _ in range(1, max_iter):
        r1 = rng.random((n_particles, dim))
        r2 = rng.random((n_particles, dim))
        vel = w * vel + c1 * r1 * (pbest - pos) + c2 * r2 * (gbest - pos)
        pos = _clip(pos + vel)
        for j in range(n_particles):
            fj = rosenbrock(pos[j])
            if fj < pbest_f[j]:
                pbest[j], pbest_f[j] = pos[j].copy(), fj
                if fj < gbest_f:
                    gbest, gbest_f = pos[j].copy(), fj
        history.append(gbest_f)
    return history


def glue(rng: np.random.Generator, max_iter: int = MAX_ITER) -> list[float]:
    """Generalised Likelihood Uncertainty Estimation (Monte Carlo sampling)."""
    best_f = np.inf
    history: list[float] = []
    for _ in range(max_iter):
        x = rng.uniform(BOUNDS[:, 0], BOUNDS[:, 1])
        f = rosenbrock(x)
        if f < best_f:
            best_f = f
        history.append(best_f)
    return history


def sobol_opt(rng: np.random.Generator, max_iter: int = MAX_ITER) -> list[float]:
    """Sobol-sequence quasi-random search with local refinement."""
    dim = BOUNDS.shape[0]
    # Generate Sobol-like low-discrepancy samples via Halton sequence
    def halton(index: int, base: int) -> float:
        result, f = 0.0, 1.0
        i = index
        while i > 0:
            f /= base
            result += f * (i % base)
            i //= base
        return result

    best_f = np.inf
    x_best = np.zeros(dim)
    history: list[float] = []
    primes = [2, 3]

    for i in range(1, max_iter + 1):
        if i <= max_iter // 2:
            # Quasi-random exploration phase
            x = np.array([halton(i, primes[d]) for d in range(dim)])
            x = BOUNDS[:, 0] + x * (BOUNDS[:, 1] - BOUNDS[:, 0])
        else:
            # Local refinement around best found
            sigma = 0.1 * (BOUNDS[:, 1] - BOUNDS[:, 0]) * (1 - i / max_iter)
            x = _clip(x_best + rng.normal(0, sigma))
        f = rosenbrock(x)
        if f < best_f:
            x_best, best_f = x.copy(), f
        history.append(best_f)
    return history


# ---------------------------------------------------------------------------
# Reporting helpers
# ---------------------------------------------------------------------------

ALGORITHMS = {
    "DDS": dds,
    "PSO": pso,
    "GLUE": glue,
    "Sobol": sobol_opt,
}


def _convergence_rate(history: list[float]) -> float:
    """Fraction of improvement achieved in first 20% of iterations."""
    n20 = max(1, len(history) // 5)
    total_drop = history[0] - history[-1]
    if total_drop == 0:
        return 0.0
    early_drop = history[0] - history[n20]
    return round(early_drop / total_drop, 4)


def _results_fingerprint(rows: list[dict]) -> str:
    data = "|".join(
        f"{r['algorithm']}:{r['best_objective']:.6f}:{r['convergence_rate']:.4f}"
        for r in rows
    )
    return hashlib.md5(data.encode()).hexdigest()


def _load_previous_fingerprint() -> str | None:
    if not os.path.exists(BENCHMARK_MD):
        return None
    with open(BENCHMARK_MD) as f:
        for line in f:
            if line.startswith("<!-- fingerprint:"):
                return line.strip().split(":")[1].rstrip(" ->").strip()
    return None


def _write_markdown(rows: list[dict], fingerprint: str, timestamp: str) -> None:
    lines = [
        f"<!-- fingerprint:{fingerprint} -->",
        "# Calibration Algorithm Benchmarks",
        "",
        f"*Last updated: {timestamp} UTC*",
        "",
        "Synthetic benchmark on the **Rosenbrock** test function "
        "f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.",
        "",
        "| Algorithm | Iterations | Best Objective | Convergence Rate |",
        "|-----------|-----------|----------------|------------------|",
    ]
    for r in rows:
        lines.append(
            f"| {r['algorithm']} | {r['iterations']} "
            f"| {r['best_objective']:.6e} | {r['convergence_rate']:.2%} |"
        )
    lines += [
        "",
        "![Convergence plot](benchmark-convergence.png)",
        "",
        "*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*",
    ]
    with open(BENCHMARK_MD, "w") as f:
        f.write("\n".join(lines) + "\n")


def _write_plot(histories: dict[str, list[float]]) -> None:
    fig, ax = plt.subplots(figsize=(8, 5))
    for name, hist in histories.items():
        ax.plot(hist, label=name, linewidth=1.4)
    ax.set_xlabel("Iteration")
    ax.set_ylabel("Best Objective Value")
    ax.set_title("Calibration Algorithm Convergence — Rosenbrock Function")
    ax.set_yscale("log")
    ax.legend()
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    fig.savefig(CONVERGENCE_PNG, dpi=150)
    plt.close(fig)


def _append_history(rows: list[dict], timestamp: str) -> None:
    write_header = not os.path.exists(HISTORY_CSV)
    with open(HISTORY_CSV, "a", newline="") as f:
        w = csv.writer(f)
        if write_header:
            w.writerow(["timestamp", "algorithm", "iterations",
                         "best_objective", "convergence_rate"])
        for r in rows:
            w.writerow([timestamp, r["algorithm"], r["iterations"],
                         f"{r['best_objective']:.6e}", f"{r['convergence_rate']:.4f}"])


def _changed(old_fp: str | None, new_fp: str) -> bool:
    """Return True if fingerprint changed (> 0.1% difference handled by fingerprint)."""
    return old_fp != new_fp


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    os.makedirs(DOCS_DIR, exist_ok=True)
    rng = np.random.default_rng(SEED)
    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M")

    histories: dict[str, list[float]] = {}
    rows: list[dict] = []

    for name, func in ALGORITHMS.items():
        hist = func(rng)
        histories[name] = hist
        rows.append({
            "algorithm": name,
            "iterations": len(hist),
            "best_objective": hist[-1],
            "convergence_rate": _convergence_rate(hist),
        })

    new_fp = _results_fingerprint(rows)
    old_fp = _load_previous_fingerprint()

    # Always append to CSV history
    _append_history(rows, timestamp)

    if _changed(old_fp, new_fp):
        _write_markdown(rows, new_fp, timestamp)
        _write_plot(histories)
        print("Benchmark results updated.")
    else:
        print("Results unchanged — skipping markdown/plot update.")

    for r in rows:
        print(f"  {r['algorithm']:6s}  best={r['best_objective']:.6e}  "
              f"conv_rate={r['convergence_rate']:.2%}")


if __name__ == "__main__":
    main()

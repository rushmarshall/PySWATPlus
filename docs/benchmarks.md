<!-- fingerprint:4c569c5febb9737f07480d9fdb4391da -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-05-11 10:49 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 2.326436e-02 | 100.00% |
| PSO | 500 | 8.536294e-20 | 100.00% |
| GLUE | 500 | 5.991458e-02 | 81.67% |
| Sobol | 500 | 2.686691e-03 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*

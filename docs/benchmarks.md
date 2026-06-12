<!-- fingerprint:a6e44146abe714d5e770a5667c8c8780 -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-06-12 11:06 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 6.204004e-01 | 99.98% |
| PSO | 500 | 1.940277e-17 | 100.00% |
| GLUE | 500 | 9.021055e-01 | 99.93% |
| Sobol | 500 | 2.749013e-03 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*

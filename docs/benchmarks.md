<!-- fingerprint:e81176c01e85058e40db8955f4bacd1a -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-10-04 11:17 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 4.720681e-01 | 100.00% |
| PSO | 500 | 1.098648e-20 | 100.00% |
| GLUE | 500 | 1.157102e-01 | 99.09% |
| Sobol | 500 | 4.012662e-03 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*

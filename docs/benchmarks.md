<!-- fingerprint:76a18ccc7f3e0e1a2afaf6b8523715c3 -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-05-29 10:56 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 1.530795e+00 | 99.93% |
| PSO | 500 | 3.723058e-17 | 100.00% |
| GLUE | 500 | 3.069367e-01 | 99.97% |
| Sobol | 500 | 1.627677e-04 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*

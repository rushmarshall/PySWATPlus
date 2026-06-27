<!-- fingerprint:284aed12cd4630312b36ed6ec55b8013 -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-06-27 10:28 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 1.527178e+00 | 100.00% |
| PSO | 500 | 9.870449e-22 | 100.00% |
| GLUE | 500 | 5.575060e-01 | 100.00% |
| Sobol | 500 | 3.597337e-03 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*

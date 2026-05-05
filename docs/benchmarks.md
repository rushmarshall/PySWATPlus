<!-- fingerprint:1d3f5149bfa50713388e1e3d3cfee1b5 -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-05-05 10:22 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 7.744272e-03 | 100.00% |
| PSO | 500 | 2.698711e-20 | 100.00% |
| GLUE | 500 | 1.160967e+00 | 100.00% |
| Sobol | 500 | 4.451082e-04 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*

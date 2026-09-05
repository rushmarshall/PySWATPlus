<!-- fingerprint:3c7879a3d68678d7f1735dd0cda2970e -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-09-05 09:49 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 1.408140e-01 | 100.00% |
| PSO | 500 | 1.175292e-19 | 100.00% |
| GLUE | 500 | 1.201229e+00 | 99.57% |
| Sobol | 500 | 5.507695e-04 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*

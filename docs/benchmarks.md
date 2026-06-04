<!-- fingerprint:b38dcffbf9ccb0b02596dc7be988e2aa -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-06-04 10:50 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 5.331399e-01 | 100.00% |
| PSO | 500 | 1.118618e-22 | 100.00% |
| GLUE | 500 | 2.038229e-02 | 100.00% |
| Sobol | 500 | 3.117396e-02 | 99.63% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*

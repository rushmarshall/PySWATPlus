<!-- fingerprint:5dc6dbc564191d2c510c180153d1712d -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-05-12 10:39 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 7.129175e-03 | 100.00% |
| PSO | 500 | 2.247215e-20 | 100.00% |
| GLUE | 500 | 5.832391e-02 | 100.00% |
| Sobol | 500 | 8.222542e-04 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*

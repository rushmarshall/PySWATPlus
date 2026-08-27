<!-- fingerprint:44e93c3f2e13cbcdb7b0d336bcfae5fd -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-08-27 13:12 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 8.421305e-02 | 99.34% |
| PSO | 500 | 6.344690e-21 | 100.00% |
| GLUE | 500 | 4.141646e-01 | 99.97% |
| Sobol | 500 | 1.357177e-03 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*

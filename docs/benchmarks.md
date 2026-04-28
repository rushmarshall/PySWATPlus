<!-- fingerprint:27fb79232a3eb61e869297fbffdfab37 -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-04-28 10:28 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 4.623627e-01 | 100.00% |
| PSO | 500 | 9.975878e-18 | 100.00% |
| GLUE | 500 | 5.871365e-02 | 99.97% |
| Sobol | 500 | 5.524662e-03 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*

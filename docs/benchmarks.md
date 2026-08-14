<!-- fingerprint:fc4a64af18c24ab5b68f6b94cd317332 -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-08-14 10:10 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 1.089829e-02 | 100.00% |
| PSO | 500 | 2.382975e-20 | 100.00% |
| GLUE | 500 | 1.079982e+00 | 99.99% |
| Sobol | 500 | 4.608606e-02 | 99.63% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*

<!-- fingerprint:9bc14c48ca315f19dd2606de9be430cf -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-10-22 09:53 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 2.898315e-01 | 100.00% |
| PSO | 500 | 5.864039e-17 | 100.00% |
| GLUE | 500 | 1.208541e+00 | 99.99% |
| Sobol | 500 | 3.322672e-03 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*

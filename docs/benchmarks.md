<!-- fingerprint:fc47d53ab0dc0befcdd7ab384f68ea07 -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-08-06 10:40 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 3.529772e-01 | 99.85% |
| PSO | 500 | 5.025236e-21 | 100.00% |
| GLUE | 500 | 1.202411e-02 | 100.00% |
| Sobol | 500 | 1.184962e-03 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*

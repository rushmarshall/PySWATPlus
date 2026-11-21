<!-- fingerprint:cbb866986023af177ea30027fe32ab1e -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-11-21 09:50 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 7.415398e-05 | 99.98% |
| PSO | 500 | 2.033022e-21 | 100.00% |
| GLUE | 500 | 5.321255e-01 | 98.22% |
| Sobol | 500 | 4.612887e-02 | 99.63% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*

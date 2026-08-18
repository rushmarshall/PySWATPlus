<!-- fingerprint:d51558645958ad1458b934462dfaddf0 -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-08-18 09:57 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 6.367051e-01 | 99.09% |
| PSO | 500 | 6.001056e-23 | 100.00% |
| GLUE | 500 | 2.354336e-01 | 99.98% |
| Sobol | 500 | 3.757441e-02 | 99.63% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*

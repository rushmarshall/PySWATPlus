<!-- fingerprint:7eba6973268264aba1f90cbea1217e59 -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-10-16 09:50 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 2.084369e-02 | 99.94% |
| PSO | 500 | 3.551438e-21 | 100.00% |
| GLUE | 500 | 7.168639e-02 | 100.00% |
| Sobol | 500 | 2.131025e-03 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*

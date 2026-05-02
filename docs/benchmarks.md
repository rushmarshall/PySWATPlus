<!-- fingerprint:ebca62a0c39f74066a53d9d91bcd08d2 -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-05-02 10:07 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 3.238120e-01 | 100.00% |
| PSO | 500 | 5.461352e-21 | 100.00% |
| GLUE | 500 | 4.281044e-02 | 100.00% |
| Sobol | 500 | 5.196088e-04 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*

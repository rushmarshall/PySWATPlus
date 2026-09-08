<!-- fingerprint:69339ea27f47e412adadde21a57cf5d8 -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-09-08 09:49 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 1.490343e+00 | 100.00% |
| PSO | 500 | 1.223643e-20 | 100.00% |
| GLUE | 500 | 6.519327e-02 | 99.57% |
| Sobol | 500 | 3.468061e-02 | 99.63% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*

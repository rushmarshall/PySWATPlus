<!-- fingerprint:7a12ffef8d634181486c770223f3defd -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-11-06 09:50 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 9.979912e+00 | 99.94% |
| PSO | 500 | 1.109112e-21 | 100.00% |
| GLUE | 500 | 4.169231e-02 | 100.00% |
| Sobol | 500 | 3.605468e-02 | 99.63% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*

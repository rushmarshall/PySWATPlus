<!-- fingerprint:f65c4c3d6a7345575fa8eb0b2b245d8b -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-10-23 09:52 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 3.490572e-02 | 99.99% |
| PSO | 500 | 6.476698e-20 | 100.00% |
| GLUE | 500 | 1.024345e+00 | 100.00% |
| Sobol | 500 | 1.591734e-02 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*

<!-- fingerprint:07e66aec8946510084443b6c8634ccf1 -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-10-08 09:56 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 1.287989e-02 | 99.98% |
| PSO | 500 | 9.800860e-25 | 100.00% |
| GLUE | 500 | 3.703019e-01 | 99.98% |
| Sobol | 500 | 2.276737e-03 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*

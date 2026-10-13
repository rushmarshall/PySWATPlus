<!-- fingerprint:fadbdc3c2609ad628ade3850af7d5441 -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-10-13 09:56 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 5.248831e-01 | 99.98% |
| PSO | 500 | 2.524708e-19 | 100.00% |
| GLUE | 500 | 7.370008e-01 | 99.97% |
| Sobol | 500 | 2.593468e-04 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*

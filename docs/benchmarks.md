<!-- fingerprint:4f5238eb998f173518ab086cdc72a757 -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-09-18 09:49 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 5.805669e-01 | 100.00% |
| PSO | 500 | 2.065294e-21 | 100.00% |
| GLUE | 500 | 1.303917e-02 | 100.00% |
| Sobol | 500 | 8.842381e-05 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*

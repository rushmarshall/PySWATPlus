<!-- fingerprint:28777d37853dfadda4da1efb32b2ec51 -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-06-22 11:42 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 2.976353e-01 | 100.00% |
| PSO | 500 | 4.826485e-20 | 100.00% |
| GLUE | 500 | 1.559422e+00 | 99.97% |
| Sobol | 500 | 2.704541e-03 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*

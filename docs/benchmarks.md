<!-- fingerprint:0195e68e9ea210a78dac4b8806ae572a -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-10-11 09:51 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 2.897221e-01 | 100.00% |
| PSO | 500 | 2.269482e-21 | 100.00% |
| GLUE | 500 | 1.135052e+00 | 100.00% |
| Sobol | 500 | 1.240621e-03 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*

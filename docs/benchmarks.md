<!-- fingerprint:66fa650c1730e33033ff3fc6b583fa82 -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-09-21 09:51 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 7.009854e-01 | 99.99% |
| PSO | 500 | 4.339332e-17 | 100.00% |
| GLUE | 500 | 4.672550e-01 | 99.97% |
| Sobol | 500 | 2.637245e-02 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*

<!-- fingerprint:c2b14927d76f153a058ddcb00fca31ef -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-06-20 10:38 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 9.699745e-01 | 100.00% |
| PSO | 500 | 1.522173e-18 | 100.00% |
| GLUE | 500 | 6.561615e-01 | 99.98% |
| Sobol | 500 | 5.801335e-03 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*

<!-- fingerprint:9317a78fe685287face3037e96fed437 -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-09-25 09:50 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 1.672370e-01 | 100.00% |
| PSO | 500 | 1.516795e-22 | 100.00% |
| GLUE | 500 | 6.290076e-01 | 99.57% |
| Sobol | 500 | 1.346269e-02 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*

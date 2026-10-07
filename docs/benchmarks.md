<!-- fingerprint:a7d5fcc860e5cde3d916bea3163128b5 -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-10-07 09:54 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 2.035378e-01 | 99.73% |
| PSO | 500 | 9.346818e-27 | 100.00% |
| GLUE | 500 | 2.365515e-01 | 93.05% |
| Sobol | 500 | 2.237649e-04 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*

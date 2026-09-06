<!-- fingerprint:eb1e80c13be35d299fd6090480f967f2 -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-09-06 09:49 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 2.659986e-01 | 100.00% |
| PSO | 500 | 6.468317e-21 | 100.00% |
| GLUE | 500 | 3.986377e-02 | 100.00% |
| Sobol | 500 | 1.443210e-02 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*

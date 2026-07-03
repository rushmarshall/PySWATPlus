<!-- fingerprint:e9e946743b50ecb34261ffcb76be457d -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-07-03 10:40 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 2.883020e-01 | 100.00% |
| PSO | 500 | 2.771150e-23 | 100.00% |
| GLUE | 500 | 2.815204e-02 | 99.98% |
| Sobol | 500 | 9.084507e-03 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*

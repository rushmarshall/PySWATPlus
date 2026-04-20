<!-- fingerprint:dd540895eec810eb1d914a963964f92e -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-04-20 10:21 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 1.799774e-02 | 99.95% |
| PSO | 500 | 4.645184e-19 | 100.00% |
| GLUE | 500 | 1.851138e+00 | 99.94% |
| Sobol | 500 | 2.221511e-03 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*

<!-- fingerprint:146697e291aa74d55433d880656ad40a -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-07-14 10:21 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 9.139128e-01 | 100.00% |
| PSO | 500 | 8.003972e-20 | 100.00% |
| GLUE | 500 | 9.282756e-02 | 100.00% |
| Sobol | 500 | 4.584533e-04 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*

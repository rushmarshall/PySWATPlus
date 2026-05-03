<!-- fingerprint:44c2fa13f0e91332024735c4a6feaa5a -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-05-03 10:10 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 2.473085e-03 | 100.00% |
| PSO | 500 | 3.272426e-18 | 100.00% |
| GLUE | 500 | 1.467378e-01 | 100.00% |
| Sobol | 500 | 1.505437e-02 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*

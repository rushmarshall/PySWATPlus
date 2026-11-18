<!-- fingerprint:7d19901ff112bf41cb095785582e89cb -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-11-18 09:49 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 1.632797e+00 | 98.65% |
| PSO | 500 | 3.950797e-18 | 100.00% |
| GLUE | 500 | 6.587828e-02 | 99.98% |
| Sobol | 500 | 5.379744e-04 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*

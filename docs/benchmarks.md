<!-- fingerprint:5bdad0309554168afb493d3d87bfe7e0 -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-06-21 10:53 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 2.629695e-01 | 89.55% |
| PSO | 500 | 7.329918e-22 | 100.00% |
| GLUE | 500 | 3.286398e-01 | 99.96% |
| Sobol | 500 | 1.241278e-02 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*

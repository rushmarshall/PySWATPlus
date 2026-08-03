<!-- fingerprint:36e1fcdcc2af16fdaf2cc278b539f671 -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-08-03 10:54 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 3.450055e-02 | 99.99% |
| PSO | 500 | 7.361155e-21 | 100.00% |
| GLUE | 500 | 5.111713e-01 | 97.80% |
| Sobol | 500 | 3.005616e-03 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*

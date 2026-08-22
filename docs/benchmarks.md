<!-- fingerprint:c13388eadad1f753cfa73a4c65046f79 -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-08-22 09:53 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 2.441233e-02 | 100.00% |
| PSO | 500 | 5.389844e-22 | 100.00% |
| GLUE | 500 | 4.515410e-02 | 99.99% |
| Sobol | 500 | 7.959093e-03 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*

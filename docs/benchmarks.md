<!-- fingerprint:0fb3013ba9755e2732a16b10e6d0a4fb -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-11-07 09:50 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 1.002673e-01 | 100.00% |
| PSO | 500 | 2.509977e-14 | 93.27% |
| GLUE | 500 | 1.331491e+00 | 99.82% |
| Sobol | 500 | 2.097927e-02 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*

<!-- fingerprint:77592ca296ccce6d499282db9215a57b -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-05-08 10:14 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 1.164837e-01 | 100.00% |
| PSO | 500 | 2.193520e-19 | 100.00% |
| GLUE | 500 | 2.031183e-01 | 97.44% |
| Sobol | 500 | 1.348062e-02 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*

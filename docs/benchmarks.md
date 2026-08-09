<!-- fingerprint:19ec2992d18e29469ab5a3ccbf46086d -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-08-09 09:59 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 6.843898e-03 | 100.00% |
| PSO | 500 | 3.697089e-21 | 100.00% |
| GLUE | 500 | 1.314166e+00 | 99.87% |
| Sobol | 500 | 1.728185e-02 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*

<!-- fingerprint:895dec37292991349db48a496c5902aa -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-08-07 10:07 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 5.151081e-02 | 100.00% |
| PSO | 500 | 9.399600e-19 | 100.00% |
| GLUE | 500 | 2.770696e-01 | 99.99% |
| Sobol | 500 | 3.379763e-03 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*

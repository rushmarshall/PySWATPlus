<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=0:111111,30:333333,60:666666,100:999999&height=180&section=header&text=PySWATPlus&fontSize=42&fontColor=FFFFFF&animation=fadeIn&fontAlignY=36&desc=SWAT%2B%20Watershed%20Model%20Calibration%20%26%20Validation%20Toolkit&descSize=14&descColor=CCCCCC&descAlignY=56"/>

<p align="center">
<img src="https://img.shields.io/badge/Python-3.9+-333333?style=flat-square&logo=python&logoColor=white" alt="Python"/>
<img src="https://img.shields.io/badge/License-MIT-333333?style=flat-square" alt="License"/>
<img src="https://img.shields.io/badge/SWAT+-333333?style=flat-square" alt="SWAT+"/>
<img src="https://img.shields.io/badge/Streamlit-UI-333333?style=flat-square&logo=streamlit&logoColor=white" alt="Streamlit"/>
<img src="https://img.shields.io/badge/CI-passing-333333?style=flat-square" alt="CI"/>
</p>

---

## Overview

**PySWATPlus** is a Python framework for calibrating, validating, and analyzing SWAT+ watershed models. It provides multiple optimization algorithms (DDS, PSO, GLUE), global sensitivity analysis (Sobol, Morris), and an interactive Streamlit dashboard for managing calibration workflows.

Built for hydrologists and water resources engineers who need reproducible, efficient model calibration with statistical rigor.

---

## Features

- **Multi-Algorithm Calibration** — DDS (Dynamically Dimensioned Search), PSO (Particle Swarm Optimization), GLUE (Generalized Likelihood Uncertainty Estimation)
- **Global Sensitivity Analysis** — Sobol variance decomposition, Morris elementary effects
- **Multi-Objective Optimization** — Pareto-optimal parameter sets with NSE, KGE, PBIAS, RMSE
- **Parallel Execution** — Concurrent SWAT+ simulations with configurable worker pools
- **Interactive Dashboard** — Streamlit UI for project setup, parameter management, and result visualization
- **Validation Framework** — Split-sample, k-fold, and multi-site validation with statistical tests
- **SWAT+ Native** — Direct cal_parms.cal editing, output parsing, and project management

---

## Installation

```bash
pip install pyswatplus
```

Or from source:

```bash
git clone https://github.com/rushmarshall/PySWATPlus.git
cd PySWATPlus
pip install -e ".[dev]"
```

---

## Quick Start

### Command Line

```python
from pyswatplus import Calibrator, SWATProject

project = SWATProject("path/to/swatplus/model")

calibrator = Calibrator(
    project=project,
    algorithm="dds",
    objective="kge",
    max_iterations=1000,
    n_workers=4,
)

# Define parameter bounds
calibrator.add_parameter("cn2", -0.3, 0.3, method="relative")
calibrator.add_parameter("esco", 0.0, 1.0, method="replace")
calibrator.add_parameter("alpha_bf", 0.0, 1.0, method="replace")

# Run calibration
results = calibrator.run(
    observed="observed_flow.csv",
    warmup_years=2,
    calibration_period=("2010-01-01", "2015-12-31"),
)

print(f"Best KGE: {results.best_objective:.4f}")
results.plot_hydrograph("calibration_hydrograph.png")
results.save("calibration_results.json")
```

### Streamlit Dashboard

```bash
streamlit run src/pyswatplus/ui/app.py
```

---

## Calibration Algorithms

| Algorithm | Type | Best For | Parameters |
|:----------|:-----|:---------|:-----------|
| DDS | Single-objective | Fast convergence, high-dimensional | `r_val`, `max_iter` |
| PSO | Single/Multi-objective | Global search, avoiding local optima | `n_particles`, `w`, `c1`, `c2` |
| GLUE | Uncertainty | Behavioral parameter identification | `n_simulations`, `threshold` |

---

## Sensitivity Analysis

```python
from pyswatplus.sensitivity import SobolAnalysis

sobol = SobolAnalysis(project=project, n_samples=1024)
sobol.add_parameter("cn2", -0.3, 0.3)
sobol.add_parameter("esco", 0.0, 1.0)
sobol.add_parameter("alpha_bf", 0.0, 1.0)

results = sobol.analyze(output_variable="streamflow")
results.plot_indices("sobol_indices.png")
```

---

## Objective Functions

| Metric | Range | Optimal | Description |
|:-------|:------|:--------|:------------|
| NSE | (-inf, 1] | 1.0 | Nash-Sutcliffe Efficiency |
| KGE | (-inf, 1] | 1.0 | Kling-Gupta Efficiency |
| PBIAS | (-inf, inf) | 0.0 | Percent Bias |
| RMSE | [0, inf) | 0.0 | Root Mean Square Error |
| R2 | [0, 1] | 1.0 | Coefficient of Determination |
| LogNSE | (-inf, 1] | 1.0 | Log-transformed NSE (low flows) |

---

## Architecture

```
pyswatplus/
├── calibration/        # Calibration engine
│   ├── algorithms/         DDS, PSO, GLUE implementations
│   ├── objective.py        Objective function library
│   └── sampler.py          Parameter sampling strategies
├── sensitivity/        # Sensitivity analysis
│   ├── sobol.py            Sobol variance decomposition
│   └── morris.py           Morris elementary effects
├── core/               # SWAT+ integration
│   ├── project.py          Project management
│   ├── runner.py           Parallel SWAT+ execution
│   ├── parser.py           Output file parsing
│   └── parameters.py       cal_parms.cal management
├── validation/         # Model validation
│   ├── splitter.py         Train/test splitting strategies
│   └── metrics.py          Statistical validation tests
└── ui/                 # Streamlit dashboard
    ├── app.py              Main application
    └── components.py       Reusable UI components
```

---

## Contributing

Contributions welcome. Please open an issue to discuss proposed changes before submitting a pull request.

```bash
git clone https://github.com/rushmarshall/PySWATPlus.git
cd PySWATPlus
pip install -e ".[dev]"
pytest tests/ -v
```

---

<p align="center">
<sub>Developed at Hydrosense Lab, University of Virginia</sub>
<br>
<sub>Part of the Global Hydrology and Water Resources research group</sub>
</p>

<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=0:999999,30:666666,60:333333,100:111111&height=100&section=footer"/>

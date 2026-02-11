Monte Carlo Credit Risk & IFRS9 Modeling Framework

1. Objective
The objective of this project is to design and implement a Python-based Monte Carlo framework for simulating portfolio credit losses and estimating Expected Credit Loss (ECL) in line with IFRS9 principles.

The project focuses on:
  - Transparent mathematical modeling
  - Clear assumptions and limitations
  - Reproducible and modular implementation

The framework is intended as a quantitative prototype, not a production system.


2. Scope
In Scope:
  - Simulation of correlated credit defaults using a one-factor Gaussian copula
  - Portfolio-level loss distribution estimation via Monte Carlo simulation
  - Discounted Expected Credit Loss (ECL) calculation

Out of Scope:
  - Calibration to real confidential bank data
  - Deep learning or black-box approaches
  - Real-time or high-frequency modeling


3. Portfolio Model
The portfolio consists of $N$ obligors characterized by:
  - Exposure at Default (EAD)
  - Probability of Default (PD)
  - Loss Given Default (LGD)
  - Maturity

The portfolio is represented by a synthetic dataset designed to reflect realistic credit characteristics.


4. Credit Risk Model
4.1 Default Model
Default events are modeled using a one-factor Gaussian copula.

The latent variable for obligor $i$ is defined as:

$$
Y_i = \sqrt{\rho}\, Z + \sqrt{1 - \rho}\, \varepsilon_i
$$

where:
- $Z \sim \mathcal{N}(0,1)$ is the systematic risk factor
- $\varepsilon_i \sim \mathcal{N}(0,1)$ is the idiosyncratic risk factor
- $\rho \in [0,1]$ denotes asset correlation

Obligor $i$ defaults if:

$$
Y_i < \Phi^{-1}(PD_i)
$$

4.2 Loss Model
Portfolio loss $L$ over the simulation horizon is defined as:

$$
L = \sum_{i=1}^{N} EAD_i \cdot LGD_i \cdot \mathbf{1}_{\{ Y_i < \Phi^{-1}(PD_i) \}}
$$


5. IFRS9 Expected Credit Loss (ECL)
Expected Credit Loss is calculated as:

$$
\mathrm{ECL} = \mathbb{E}\!\left[ \sum_{t=1}^{T} DF_t \cdot PD_t \cdot LGD_t \cdot EAD_t \right]
$$

where:
- $DF_t$ denotes discount factors
- $PD_t$ are scenario-dependent marginal default probabilities
- $LGD_t$ denotes loss given default
- $EAD_t$ denotes exposure at default

In line with IFRS9, the framework supports:

- **Stage 1 (12-month ECL)**:
  
  $$
  \mathrm{ECL}_{12m} = \mathbb{E}\!\left[ \sum_{t=1}^{12} DF_t \cdot PD_t \cdot LGD_t \cdot EAD_t \right]
  $$

- **Stage 2 (Lifetime ECL)** (simplified):
  
  $$
  \mathrm{ECL}_{LT} = \mathbb{E}\!\left[ \sum_{t=1}^{T} DF_t \cdot PD_t \cdot LGD_t \cdot EAD_t \right]
  $$


6. Scenario Analysis
The model incorporates macroeconomic scenarios affecting default probabilities:
  - Base scenario
  - Adverse scenario
  - Severe scenario

Scenario impacts are applied via multiplicative or additive PD adjustments.


7. Simulation Methodology
  - Monte Carlo simulation with configurable number of iterations
  - Vectorized implementation for performance
  - Reproducible results via fixed random seeds

Key outputs:
  - Loss distribution
  - Expected Loss
  - Value-at-Risk
  - Scenario comparison plots


8. Validation & Sensitivity Analysis
The framework includes:
  - Sensitivity analysis with respect to PD, LGD, and correlation
  - Sanity checks on loss distributions
  - Qualitative discussion of model limitations


9. Limitations
  - Simplified dependence structure (single systematic factor)
  - Stylized PD and LGD assumptions
  - No dynamic migration modeling
  - No calibration to real market or bank data

These limitations are intentional to preserve interpretability.


10. Intended Audience
This project is intended for:
  - Risk modeling discussions
  - Demonstration of applied stochastic modeling skills
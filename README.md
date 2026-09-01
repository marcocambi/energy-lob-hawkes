# Energy LOB Hawkes

This repository contains code and research notes for modeling high-frequency market microstructure, specifically looking at Limit Order Books (LOB) using multivariate Hawkes processes. 

The main goal is to study how orders influence each other in financial and energy markets—checking things like self-excitation and cross-excitation between different tick events (such as limit orders, cancellations, and market orders).

## Mathematical Model

The conditional intensity vector $\lambda_i(t)$ for event type $i$ is defined as:

$$\lambda_i(t \mid \mathcal{F}_t) = \mu_i + \sum_{j=1}^M \int_0^t \Phi_{ij}(t - s) \, dN_j(s)$$

Where:
- $\mu_i$: Baseline arrival rate for event $i$.
- $\mathcal{F}_t$: History of past events up to time $t$.
- $\Phi_{ij}(\Delta t) = \alpha_{ij} e^{-\beta_{ij} \Delta t}$: Exponential decay kernel showing how past events of type $j$ affect type $i$.

## Repository Structure

```text
energy-lob-hawkes/
├── src/
│   ├── cpp/       # C++ core engine for low-latency simulation
│   └── python/    # Python scripts for data analysis and calibration
├── data/          # Processed datasets and sample ticks
└── tests/         # Unit tests

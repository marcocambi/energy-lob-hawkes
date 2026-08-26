# Limit Order Book Dynamics and Multivariate Hawkes Processes in Energy Markets

This repository contains research code and mathematical frameworks for modeling high-frequency Limit Order Book (LOB) dynamics in energy trading venues using multivariate point processes. The study focuses on order flow self-excitation, cross-queue interactions, and transient market impact.

## Mathematical Framework

The conditional intensity process $\lambda_i(t)$ for event stream $i \in \{1, \dots, M\}$ (representing limit orders, market orders, and cancellations across sides) is defined as:

$$\lambda_i(t) = \mu_i + \sum_{j=1}^{M} \int_0^t \alpha_{ij} e^{-\beta_{ij}(t-s)} dN_j(s)$$

Where:
* $\mu_i > 0$ denotes the baseline arrival intensity for event type $i$.
* $\alpha_{ij} \ge 0$ quantifies the kernel magnitude (excitation impact of event $j$ on event $i$).
* $\beta_{ij} > 0$ controls the exponential decay rate of memory.

## Repository Layout

* `paper/`: Draft manuscripts, theoretical notes, and LaTeX source files.
* `src/`: Python modules for LOB state reconstruction, intensity estimation, and MLE parameter calibration.
* `notebooks/`: Empirical diagnostics, parameter estimation tests, and diagnostic plots.
* `data/`: High-frequency LOB snapshots and order event data.

## Setup & Dependencies

Clone the repository and set up the execution environment:

```bash
git clone [https://github.com/marcocambi/energy-lob-hawkes.git](https://github.com/marcocambi/energy-lob-hawkes.git)
cd energy-lob-hawkes
python -m venv venv
source venv/bin/activate

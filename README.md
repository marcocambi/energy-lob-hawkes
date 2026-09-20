# LOB Hawkes

This repository contains code and research notes for modeling high-frequency
market microstructure using self-exciting Hawkes processes, applied in
parallel to two domains: equity limit order books (NASDAQ/LOBSTER) and
energy markets (EPEX Spot/ICE).

The goal is to characterize temporal clustering of trade events — how the
occurrence of one event increases the short-term probability of another —
using a univariate self-exciting point process with exponential decay kernel.

## Mathematical Model

The conditional intensity for the event process is defined as:

λ(t | F_t) = μ + Σ_{T_i < t} α e^{-β(t - T_i)}

Where:
- μ: baseline arrival rate
- F_t: history of past events up to time t
- α, β: excitation and decay parameters, with stationarity requiring α/β < 1

Estimation via recursive O(N) log-likelihood (MLE), goodness-of-fit via
Papangelou time-rescaling (KS-test on rescaled inter-arrival times).

**Out of scope:** multivariate cross-excitation between event types
(limit orders, cancellations, market orders), full LOB L2/L3 reconstruction,
market impact models. These are noted as future work only, not implemented.

## Repository Structure

- `src/python/equity/` — NASDAQ/LOBSTER pipeline and estimation (Marco)
- `src/python/energy/` — EPEX Spot/ICE pipeline and estimation (Antonio)
- `src/python/common/` — shared MLE, GOF, and simulation code
- `tests/` — validation on synthetic fixtures (Ogata thinning simulator)
- `data/` — raw and processed datasets (gitignored)

# LOB Hawkes

Code and research notes for modeling high-frequency market microstructure with self-exciting Hawkes processes, applied in parallel to two domains: equity limit order books (NASDAQ/LOBSTER) and energy markets (EPEX Spot/ICE).

The goal is temporal clustering of trade events — how one event raises the short-term probability of another. A univariate self-exciting point process with exponential decay kernel handles that.

## Mathematical Model

The conditional intensity:

$$\lambda(t \mid \mathcal{F}_t) = \mu + \sum_{T_i < t} \alpha \* e^{-\beta (t - T_i)}$$

μ is the baseline arrival rate. F_t is the event history up to t. α and β are the excitation and decay parameters; stationarity requires α/β < 1.

Estimation runs on recursive O(N) log-likelihood (MLE). Goodness-of-fit via Papangelou time-rescaling, then a KS-test on the rescaled inter-arrival times.

Out of scope: multivariate cross-excitation between event types (limit orders, cancellations, market orders), full L2/L3 LOB reconstruction, market impact models. Noted as future work, not implemented.

## Repository Structure

`src/python/equity/` holds the NASDAQ/LOBSTER pipeline and estimation, Marco's side. `src/python/energy/` mirrors it for EPEX Spot/ICE, Antonio's side. `src/python/common/` carries shared MLE, GOF, and simulation code. `tests/` validates against synthetic fixtures from the Ogata thinning simulator. `data/` holds raw and processed datasets, gitignored.

import numpy as np
from scipy.optimize import minimize
from typing import import Dict, Any

## definition of hawkes_log_likelihood_recursive
def hawkes_log_likelihood_recursive(params: np.ndarray, timestamps: np.ndarray, T_end: float) -> float:
  mu, alpha, beta = params
  # Vincoli di accettabilità e branching ratio
  if(mu <= 0 or alpha <=0 or beta <= 0 or alpha >= beta):
    return 1e10
    
  # total numper of events in arrays, if the temporal windows doesn't contain any events
  N = len(timestamps)
  if(N == 0):
    return 0.0
  # difference of time from 2 separates events
  dt = np.diff(timestamps, prepend=timestamps[0])
  R = np.zeros(N)
  for i in range(1, N):
    R[i] = np.exp(-beta*dt[i])*(1+R[i-1])
  intensity_at_events = mu + alpha*R
  if(np.any(intensity_at_events<=0)):
    return 1e10
  log_sum = np.sum(np.log(intensity_at_events))
  integral_term = mu*T_end + (alpha/beta) * np.sum(1.0 - np.exp(-beta*(T-end - timestamps)))
  return -(log_sum - integral_term)

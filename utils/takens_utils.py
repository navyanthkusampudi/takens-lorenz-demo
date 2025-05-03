# utils/takens_utils.py

import numpy as np

def compute_delay_embedding(y, tau, m):
    """
    Reconstruct the phase space using Takens' time-delay embedding.
    y: 1D time series (numpy array)
    tau: time delay (int)
    m: embedding dimension (int)
    Returns: (N, m) matrix where N = len(y) - (m - 1) * tau
    """
    N = len(y) - (m - 1) * tau
    if N <= 0:
        return None
    return np.column_stack([y[i:i + N] for i in range(0, m * tau, tau)])

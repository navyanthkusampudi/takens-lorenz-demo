import numpy as np

def compute_delay_embedding(y, tau, m):
    """
    Reconstruct a phase space using Takens' delay embedding.
    """
    N = len(y) - (m - 1) * tau
    if N <= 0:
        return None
    return np.column_stack([y[i:i+N] for i in range(0, m * tau, tau)])

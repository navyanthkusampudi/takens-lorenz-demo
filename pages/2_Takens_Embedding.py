import streamlit as st
import numpy as np
from utils.takens_utils import compute_delay_embedding
from utils.plotting import plot_2d_scatter, plot_3d_scatter

st.set_page_config(page_title="Takens Embedding", layout="wide")
st.title("📉 Takens Time-Delay Embedding")

st.markdown("""
Upload a time series or use the sample sine wave below to reconstruct an attractor using Takens' theorem.
""")

# Sample signal
t = np.linspace(0, 100, 2000)
y = np.sin(t) + 0.5 * np.sin(3 * t)
st.line_chart(y[:500])

# Sidebar parameters
st.sidebar.header("Embedding Parameters")
tau = st.sidebar.slider("Delay (τ)", 1, 100, 10)
m = st.sidebar.slider("Dimension (m)", 2, 10, 3)

# Compute embedding
X = compute_delay_embedding(y, tau, m)

if X is None:
    st.error("Insufficient data for given τ and m.")
else:
    if m == 2:
        st.plotly_chart(plot_2d_scatter(X[:, 0], X[:, 1],
                        title="2D Embedding", xlabel="y(t)", ylabel=f"y(t+{tau})"), use_container_width=True)
    else:
        st.plotly_chart(plot_3d_scatter(X[:, 0], X[:, 1], X[:, 2],
                        title="3D Embedding"), use_container_width=True)

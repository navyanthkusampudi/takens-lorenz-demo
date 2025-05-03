import streamlit as st
import numpy as np
from scipy.integrate import solve_ivp

from utils.lorenz_solver import lorenz_system
from utils.takens_utils import compute_delay_embedding
from utils.plotting import plot_2d_scatter, plot_3d_scatter

st.set_page_config(page_title="Takens Embedding", layout="wide")
st.title("📉 Takens Embedding from Lorenz Attractor")

st.markdown("""
This tool reconstructs the phase space using **Takens’ theorem**, applied to the `x(t)` time series from the Lorenz system.
""")

# Sidebar: Lorenz simulation settings
st.sidebar.header("Lorenz Parameters")
sigma = st.sidebar.slider("σ (sigma)", 0.1, 20.0, 10.0)
beta = st.sidebar.slider("β (beta)", 0.1, 10.0, 8/3)
rho = st.sidebar.slider("ρ (rho)", 0.1, 100.0, 28.0)

st.sidebar.header("Initial Conditions")
x0 = st.sidebar.number_input("X0", value=1.0)
y0 = st.sidebar.number_input("Y0", value=1.0)
z0 = st.sidebar.number_input("Z0", value=1.0)

st.sidebar.header("Simulation Settings")
T = st.sidebar.slider("Simulation Time (s)", 10, 100, 40)
dt = st.sidebar.slider("Time Step", 0.001, 0.1, 0.01)

# Sidebar: Embedding parameters
st.sidebar.header("Embedding Parameters")
tau = st.sidebar.slider("Delay (τ)", 1, 100, 10)
m = st.sidebar.slider("Embedding Dimension (m)", 2, 10, 3)

# Solve Lorenz system
t_eval = np.arange(0, T, dt)
sol = solve_ivp(lambda t, y: lorenz_system(t, y, sigma, rho, beta),
                [0, T], [x0, y0, z0], t_eval=t_eval)

x = sol.y[0]  # x(t) is the observed variable

st.line_chart(x[:500])  # Show preview of x(t)

# Perform Takens Embedding
X = compute_delay_embedding(x, tau, m)

if X is None:
    st.error("τ and m produce too few data points.")
else:
    st.markdown(f"**Embedding space (m={m}, τ={tau})**")
    if m == 2:
        st.plotly_chart(plot_2d_scatter(X[:, 0], X[:, 1], title="2D Embedding", xlabel="x(t)", ylabel=f"x(t+{tau})"),
                        use_container_width=True)
    else:
        st.plotly_chart(plot_3d_scatter(X[:, 0], X[:, 1], X[:, 2], title="3D Embedding from x(t)"),
                        use_container_width=True)

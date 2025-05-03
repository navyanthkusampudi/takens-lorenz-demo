import streamlit as st
import numpy as np
from scipy.integrate import solve_ivp

from utils.lorenz_solver import lorenz_system
from utils.takens_utils import compute_delay_embedding
from utils.plotting import plot_2d_scatter, plot_3d_scatter

st.set_page_config(page_title="Takens Embedding", layout="wide")
st.title("📉 Takens Embedding from Lorenz System")

st.markdown("""
Explore how Takens' theorem allows reconstruction of the phase space from a single variable.  
Choose `x(t)`, `y(t)`, or `z(t)` from the Lorenz system to visualize and compare the original and reconstructed attractors.
""")

# --- Sidebar Controls ---

# Lorenz parameters
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

# Embedding parameters
st.sidebar.header("Embedding Parameters")
observed_var = st.sidebar.selectbox("Variable for Embedding", options=["x", "y", "z"])
tau = st.sidebar.slider("Delay (τ)", 1, 100, 10)
m = st.sidebar.slider("Embedding Dimension (m)", 2, 10, 3)

# --- Solve Lorenz System ---
t_eval = np.arange(0, T, dt)
sol = solve_ivp(lambda t, y: lorenz_system(t, y, sigma, rho, beta),
                [0, T], [x0, y0, z0], t_eval=t_eval)

x, y, z = sol.y

# Choose variable
var_map = {"x": x, "y": y, "z": z}
signal = var_map[observed_var]

# Preview signal
st.subheader(f"📈 Observed Variable: {observed_var}(t)")
st.line_chart(signal[:500])

# --- Original Attractor ---
st.subheader("🌀 Original Lorenz Attractor (x, y, z)")
orig_fig = plot_3d_scatter(x, y, z, title="Original Lorenz Attractor")
st.plotly_chart(orig_fig, use_container_width=True)

# --- Takens Embedding ---
X = compute_delay_embedding(signal, tau, m)

if X is None:
    st.error("τ and m produce too few data points.")
else:
    st.subheader(f"🔁 Reconstructed Attractor from {observed_var}(t)")
    if m == 2:
        st.plotly_chart(plot_2d_scatter(X[:, 0], X[:, 1],
                                        title=f"2D Embedding from {observed_var}(t)",
                                        xlabel=f"{observed_var}(t)",
                                        ylabel=f"{observed_var}(t+{tau})"),
                        use_container_width=True)
    else:
        st.plotly_chart(plot_3d_scatter(X[:, 0], X[:, 1], X[:, 2],
                                        title=f"3D Embedding from {observed_var}(t)"),
                        use_container_width=True)

import streamlit as st
import numpy as np
from scipy.integrate import solve_ivp
from utils.lorenz_solver import lorenz_system
from utils.plotting import plot_3d_scatter

st.set_page_config(page_title="Lorenz Attractor", layout="wide")
st.title("🌀 Lorenz Attractor Explorer")

# Sidebar UI
st.sidebar.header("Lorenz Parameters")
sigma = st.sidebar.slider("σ (sigma)", 0.1, 20.0, 10.0, 0.1)
beta = st.sidebar.slider("β (beta)", 0.1, 10.0, 8/3, 0.1)
rho = st.sidebar.slider("ρ (rho)", 0.1, 100.0, 28.0, 0.1)

st.sidebar.header("Initial Conditions")
x0 = st.sidebar.number_input("X0", value=1.0)
y0 = st.sidebar.number_input("Y0", value=1.0)
z0 = st.sidebar.number_input("Z0", value=1.0)

st.sidebar.header("Simulation Settings")
T = st.sidebar.slider("Simulation Time (s)", 10, 100, 40)
dt = st.sidebar.slider("Time Step", 0.001, 0.1, 0.01)

# Solve system
t_eval = np.arange(0, T, dt)
sol = solve_ivp(lambda t, y: lorenz_system(t, y, sigma, rho, beta),
                [0, T], [x0, y0, z0], t_eval=t_eval)
x, y, z = sol.y

# Plot
fig = plot_3d_scatter(x, y, z, title="Lorenz Attractor")
st.plotly_chart(fig, use_container_width=True)

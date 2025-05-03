import streamlit as st
import numpy as np
from utils.takens_utils import compute_delay_embedding
from utils.plotting import plot_2d_scatter, plot_3d_scatter

st.set_page_config(page_title="Synthetic Birdsong", layout="wide")
st.title("🎶 Synthetic Birdsong Generator")

st.markdown("""
This tool simulates a birdsong-like signal using amplitude and frequency modulation.  
You can adjust both components and visualize the resulting attractor using Takens embedding.
""")

# Sidebar controls
st.sidebar.header("Signal Settings")
duration = st.sidebar.slider("Duration (s)", 1.0, 10.0, 2.5, 0.5)
fs = st.sidebar.slider("Sampling Frequency", 100, 2000, 400, 100)

st.sidebar.subheader("Amplitude Envelope")
amp_freq = st.sidebar.slider("Envelope frequency (Hz)", 0.1, 5.0, 0.3, 0.1)

st.sidebar.subheader("Frequency Modulation")
base_freq = st.sidebar.slider("Base frequency (Hz)", 5.0, 50.0, 28.0, 1.0)
mod_depth = st.sidebar.slider("Modulation depth", 0.0, 20.0, 2.0, 0.5)
mod_freq = st.sidebar.slider("Modulation frequency (Hz)", 0.1, 10.0, 0.9, 0.1)

# Generate synthetic signal
t = np.linspace(0, duration, int(fs * duration))
A = 0.5 + 0.5 * np.sin(2 * np.pi * amp_freq * t)
f_mod = base_freq + mod_depth * np.sin(2 * np.pi * mod_freq * t)
phase = 2 * np.pi * np.cumsum(f_mod) / fs
y = A * np.sin(phase)

# Show waveform
st.subheader("📈 Generated Signal")
st.line_chart(y[:1000])  # preview

# Takens embedding settings
st.sidebar.header("Takens Embedding")
tau = st.sidebar.slider("Delay (τ)", 1, 100, 2,)
m = st.sidebar.slider("Embedding Dimension (m)", 2, 10, 7)

X = compute_delay_embedding(y, tau, m)

if X is None:
    st.error("τ and m produce too few points for this signal length.")
else:
    st.subheader("🌀 Takens Embedding")
    if m == 2:
        st.plotly_chart(plot_2d_scatter(X[:, 0], X[:, 1],
                                        title="2D Embedding",
                                        xlabel="y(t)", ylabel=f"y(t+{tau})"), use_container_width=True)
    else:
        st.plotly_chart(plot_3d_scatter(X[:, 0], X[:, 1], X[:, 2],
                                        title="3D Embedding"), use_container_width=True)

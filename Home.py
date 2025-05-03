import streamlit as st

st.set_page_config(page_title="Birdsong Dynamics", layout="wide")
st.title("Takens & Lorenz: Visualizing Dynamical Systems")

st.markdown("---")

st.markdown("""
Welcome to this interactive exploration of **nonlinear systems**.

- Use the **Lorenz Attractor** page to explore a chaotic system.
- Use the **Takens Embedding** page to reconstruct dynamics from a single signal.
""")

Takens & Lorenz: Visualizing Dynamical Systems

This project explores the hidden structure of nonlinear systems through interactive visualizations built with Streamlit. It includes:

- Lorenz Attractor Explorer – Adjust parameters and initial conditions to explore the dynamics of the Lorenz system.
- Takens Time-Delay Embedding – Reconstruct attractors from a single time series (like the Lorenz x-variable or birdsong) using delay coordinates.

Live Demo Links (to be added later):
- Lorenz Attractor App: [COMING SOON]
- Takens Embedding App: [COMING SOON]

Project Structure:
takens-lorenz-demo/
├── Home.py                     -> Main landing page for the app
├── pages/
│   ├── 1_Lorenz_Attractor.py   -> App for Lorenz system visualization
│   └── 2_Takens_Embedding.py   -> App for delay embedding visualization
├── utils/
│   ├── lorenz_solver.py        -> Contains the Lorenz system equations
│   ├── takens_utils.py         -> Embedding computation logic
│   └── plotting.py             -> Reusable plotting functions
├── requirements.txt            -> Python package dependencies
├── README.md                   -> Project description and instructions

How to Run Locally:

1. Clone the repository:
   git clone https://github.com/yourusername/takens-lorenz-demo.git
   cd takens-lorenz-demo

2. Install the required packages:
   pip install -r requirements.txt

3. Run the Streamlit app:
   streamlit run Home.py

Use the sidebar to switch between:
- Lorenz Attractor
- Takens Embedding

Concepts:

Lorenz Attractor:
A system of three nonlinear differential equations introduced by Edward Lorenz in 1963. It models fluid convection and exhibits chaotic behavior under certain parameters. The resulting attractor is a hallmark example of deterministic chaos.

Takens Embedding:
Introduced by Floris Takens in 1981, this method allows us to reconstruct a system’s state space from a single observed variable. By plotting time-delayed versions of a signal in a higher-dimensional space, we recover a geometric representation (the attractor) that reflects the system’s dynamics.

Features:
- Interactive sliders for parameters (σ, ρ, β), initial conditions, time step, and simulation time
- Adjustable embedding dimension (m) and delay (τ)
- 2D and 3D visualizations with Plotly
- Modular utilities for reuse across apps

Future Features:
- Upload your own .csv or .wav time series
- Attractor reconstruction from real birdsong data
- Analysis of attractor properties: Lyapunov exponents, correlation dimension, etc.

Credits:
- Edward Lorenz – Lorenz system and chaos theory
- Floris Takens – Embedding theorem
- Xeno-Canto – Source of birdsong recordings
- Streamlit – For rapid app development

License:
MIT License
(c) 2025 [Navyanth Kusampudi]
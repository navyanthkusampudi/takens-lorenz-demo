import numpy as np
import plotly.graph_objects as go

def plot_syrinx_membrane(amplitude=0.6, frequency=30, duration=0.1, fs=1000):
    """
    Simulate vibrating membrane as a sine wave over time.
    amplitude: height of vibration
    frequency: frequency of oscillation (Hz)
    """
    t = np.linspace(0, duration, int(fs * duration))
    y = amplitude * np.sin(2 * np.pi * frequency * t)

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=t,
        y=y,
        mode="lines",
        line=dict(color="royalblue", width=3),
        name="Membrane"
    ))

    fig.update_layout(
        title="Syrinx Membrane Vibration",
        xaxis_title="Time",
        yaxis_title="Displacement",
        margin=dict(l=40, r=40, b=40, t=40),
        height=300
    )

    return fig

import plotly.graph_objects as go

def plot_2d_scatter(x, y, title="2D Scatter", xlabel="x", ylabel="y", color='blue'):
    fig = go.Figure()

    # Add gray connecting line
    fig.add_trace(go.Scatter(
        x=x, y=y,
        mode='lines',
        line=dict(color='lightgray', width=1),
        name='trajectory'
    ))

    # Add data points
    fig.add_trace(go.Scatter(
        x=x, y=y,
        mode='markers',
        marker=dict(color=color, size=4),
        name='points'
    ))

    fig.update_layout(
        title=title,
        xaxis_title=xlabel,
        yaxis_title=ylabel,
        margin=dict(l=40, r=40, b=40, t=40)
    )

    return fig


def plot_3d_scatter(x, y, z, title="3D Scatter", color='blue'):
    fig = go.Figure()

    # Add gray line
    fig.add_trace(go.Scatter3d(
        x=x, y=y, z=z,
        mode='lines',
        line=dict(color='lightgray', width=1),
        name='trajectory'
    ))

    # Add blue points
    fig.add_trace(go.Scatter3d(
        x=x, y=y, z=z,
        mode='markers',
        marker=dict(color=color, size=3),
        name='points'
    ))

    fig.update_layout(
        title=title,
        scene=dict(xaxis_title='x(t)', yaxis_title='x(t+τ)', zaxis_title='x(t+2τ)'),
        margin=dict(l=0, r=0, b=0, t=40)
    )

    return fig



def plot_time_series(y, title="Time Series", xlabel="Sample Index", ylabel="Amplitude", color='blue'):
    x = np.arange(len(y))  # use indices as x-axis

    fig = go.Figure()

    # Line
    fig.add_trace(go.Scatter(
        x=x, y=y,
        mode='lines',
        line=dict(color='lightgray', width=1),
        name='signal'
    ))

    # Markers
    fig.add_trace(go.Scatter(
        x=x, y=y,
        mode='markers',
        marker=dict(color=color, size=3),
        name='samples'
    ))

    fig.update_layout(
        title=title,
        xaxis_title=xlabel,
        yaxis_title=ylabel,
        margin=dict(l=40, r=40, b=40, t=40)
    )

    return fig

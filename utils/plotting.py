import plotly.graph_objects as go

def plot_3d_scatter(x, y, z, title="3D Scatter Plot", color='blue'):
    fig = go.Figure()
    fig.add_trace(go.Scatter3d(x=x, y=y, z=z, mode='lines', line=dict(color=color)))
    fig.update_layout(
        title=title,
        scene=dict(xaxis_title='X', yaxis_title='Y', zaxis_title='Z'),
        margin=dict(l=0, r=0, b=0, t=40)
    )
    return fig

def plot_2d_scatter(x, y, title="2D Scatter Plot", xlabel="x", ylabel="y", color='blue'):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=y, mode='lines+markers',
                             line=dict(color=color), marker=dict(size=4)))
    fig.update_layout(
        title=title,
        xaxis_title=xlabel,
        yaxis_title=ylabel,
        margin=dict(l=40, r=40, b=40, t=40)
    )
    return fig

import json
from os import listdir
from os.path import dirname, abspath

import plotly.graph_objects as go


def max_of_property(data, property):
    return max(map(lambda e: max(e[property]), data))


def load_data(data_dir):
    datadir = f"{dirname(abspath(__file__))}/{data_dir}"
    files = listdir(datadir)
    files.sort()
    data = []

    for filename in files:
        with open(f"{datadir}/{filename}") as file:
            data.append(json.load(file))

    return data


fig = go.Figure()

data = load_data("data")

# Add traces, one for each slider step
for step in data:
    fig.add_trace(
        go.Scatter(
            visible=False,
            mode='markers',
            marker=dict(
                size=7,
                cmin=0,
                cmax=100,
                color=step["coverage"],
                colorscale='RdYlGn',
                colorbar=dict(
                    title=dict(
                        text='Code Coverage',
                        side='right')),
                showscale=True
            ),
            name="",
            text=step["files"],
            x=step["churn"],
            y=step["complexity"]))

# Make first trace visible
fig.data[0].visible = True

# Create and add slider
steps = []
for i in range(len(data)):
    step = dict(
        method="restyle",
        args=["visible", [False] * len(data)],
        label=f"{data[i]['version']} ({data[i]['date']})"
    )
    step["args"][1][i] = True  # Toggle i'th trace to "visible"
    steps.append(step)

sliders = [dict(
    active=0,
    currentvalue={"prefix": "Version: "},
    pad=dict(t=50),
    steps=steps
)]

fig.update_layout(
    xaxis_title="Churn (over previous 12 months)",
    yaxis_title="Cyclomatic Code Complexity",
    height=800,
    sliders=sliders
)

# fig.update_xaxes(range=[-0.05, max_of_property(data, "churn") + 0.05])
# fig.update_yaxes(range=[-0.5, max_of_property(data, "complexity") + 0.5])
fig.update_xaxes(range=[-0.05, max_of_property(data, "churn") + 0.05])
fig.update_yaxes(type='log')

fig.show()

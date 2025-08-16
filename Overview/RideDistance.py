import pandas as pd
import plotly.graph_objects as go

df = pd.read_csv("../data.csv")
flow_counts = df.groupby(['Pickup Location', 'Drop Location']).size().reset_index(name='count')

locations = list(pd.unique(flow_counts[['Pickup Location', 'Drop Location']].values.ravel()))

location_indices = {loc: i for i, loc in enumerate(locations)}


sources = flow_counts['Pickup Location'].map(location_indices)
targets = flow_counts['Drop Location'].map(location_indices)
values = flow_counts['count']


fig = go.Figure(data=[go.Sankey(
    node=dict(
        pad=20,
        thickness=20,
        line=dict(color="black", width=0.5),
        label=locations,
        color="lightblue"
    ),
    link=dict(
        source=sources,
        target=targets,
        value=values
    )
)])

fig.update_layout(title_text="Przepływ kursów: Pickup → Drop Location", font_size=12)
fig.show()

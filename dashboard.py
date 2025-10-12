# app.py
import pandas as pd
from dash import Dash, dcc, html
import plotly.express as px

# Load data
df = pd.read_excel("SOM_Country_Clusters.xlsx")

# Create the app
app = Dash(__name__)
server = app.server  # Needed for hosting on Render or Heroku later

# Create choropleth map
fig = px.choropleth(
    df,
    locations="Country",
    locationmode="country names",
    color="Category",
    title="🌍 SOM Country Clustering by Category",
    color_continuous_scale="Viridis",
    hover_name="Country"
)

# Layout
app.layout = html.Div([
    html.H1("Self-Organizing Map (SOM) Classification of 195 Countries", style={'textAlign': 'center'}),
    html.P("Explore how countries are grouped into categories based on 32 economic indicators.", style={'textAlign': 'center'}),
    dcc.Graph(figure=fig)
])

# Run
if __name__ == "__main__":
    app.run_server(debug=True)

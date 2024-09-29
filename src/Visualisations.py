import pydeck as pdk
import streamlit as st

class ScatterplotVisualizer:
    def __init__(self, data):
        self.data = data.get_data()
        self.scatterplot_layer = self.create_scatterplot_layer()
        self.view_state = self.create_view_state()
        self.tooltip = self.create_tooltip()

    def create_scatterplot_layer(self):
        return pdk.Layer(
            "ScatterplotLayer",
            data=self.data,
            get_position='[Longitude, Latitude]',
            get_radius=10000,
            get_color='[200, 30, 0, 160]',
            pickable=True,
            tooltip=True,
            get_elevation="Elevation",
        )

    def create_view_state(self):
        return pdk.ViewState(
            latitude=float(self.data["Latitude"].mean()),
            longitude=float(self.data["Longitude"].mean()),
            zoom=3,
            pitch=0,
        )

    def create_tooltip(self):

        return {
            "html": "<b>Site Number:</b> {site_number}<br/>"
                "<b>Site Name:</b> {site_name}<br/>"
                "<b>Avg Max Temp (°C):</b> {avg_max_temp}<br/>"
                "<b>Avg Min Temp (°C):</b> {avg_min_temp}<br/>"
                "<b>Avg Mean Temp (°C):</b> {avg_mean_temp}<br/>"
                "<b>Elevation:</b> {Elevation} meters<br/>"
                "<b>Koppen Classification:</b> {Koppen_Classification}",
            "style": {
            "backgroundColor": "steelblue",
            "color": "white"
            }
        }

    def render(self):
        r = pdk.Deck(layers=[self.scatterplot_layer], initial_view_state=self.view_state, tooltip=self.tooltip)
        st.pydeck_chart(r)


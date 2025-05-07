import pandas as pd
import streamlit as st
import plotly.express as px

# Load data
df = pd.read_csv("data/processed/listings.csv")
df = df.dropna(subset=["price"])


st.title("Airbnb Dashboard 🌍")

# Liste des quartiers avec une option "Tous"
neighbourhoods = ["Tous"] + sorted(df["neighbourhood_cleansed"].dropna().unique().tolist())

# Sidebar filter
selected_neighbourhood = st.sidebar.selectbox("Choisir un quartier", neighbourhoods)

# Appliquer le filtre uniquement si un quartier spécifique est sélectionné
if selected_neighbourhood != "Tous":
    filtered_df = df[df["neighbourhood_cleansed"] == selected_neighbourhood]
else:
    filtered_df = df

# Afficher la carte colorée par prix
st.subheader("Carte des logements (colorée par prix)")

fig_map = px.scatter_mapbox(
    filtered_df,
    lat="latitude",
    lon="longitude",
    color="price",
    size_max=10,
    zoom=11,
    mapbox_style="carto-positron",
    hover_name="name",
    hover_data={"price": True, "latitude": False, "longitude": False}
)

st.plotly_chart(fig_map, use_container_width=True)

# Boxplot des prix
st.subheader("Distribution des prix")
fig = px.box(filtered_df, x="neighbourhood_cleansed", y="price", title="Répartition des prix des logements")
st.plotly_chart(fig)

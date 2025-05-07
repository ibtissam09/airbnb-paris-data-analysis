import pandas as pd
import streamlit as st
import plotly.express as px

# Load data
df = pd.read_csv("data/processed/listings.csv")

st.title("Airbnb Dashboard 🌍")

# Sidebar filters
city = st.sidebar.selectbox("Select a Neighbourhood", df["neighbourhood_cleansed"].dropna().unique())

filtered_df = df[df["neighbourhood_cleansed"] == city]

# Show map
st.subheader("Map of Listings")
st.map(filtered_df[["latitude", "longitude"]])

# Show price distribution using a boxplot
st.subheader("Price Distribution")
fig = px.box(filtered_df, x="neighbourhood_cleansed", y="price", title="Price Distribution Boxplot")
st.plotly_chart(fig)
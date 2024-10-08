import pandas as pd
import streamlit as st
from bokeh.models import ColumnDataSource
from bokeh.plotting import figure

# Streamlit configurations
st.title("Bokeh on Streamlit")
st.markdown("Upload your .parquet files to visualize them.")

st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    .reportview-container .main .block-container{padding-top: 0rem;}
    header {visibility: hidden;}
    div[role="progressbar"] {
        visibility: hidden;
    }
    </style>
    """, unsafe_allow_html=True)

# File Upload
uploaded_file = st.file_uploader("Choose a Parquet file", type="parquet")
if uploaded_file is not None:
    df = pd.read_parquet(uploaded_file)

    if st.button("Create Bokeh plot"):
        source = ColumnDataSource(df)

        # Example of using Bokeh to create an interactive plot
        p = figure()
        p.scatter(x="x", y="y", source=source)

        # Embed plot into Streamlit
        st.bokeh_chart(p)

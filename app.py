import streamlit as st
from app_pages.multipage import MultiPage

# load pages scripts
from app_pages.page_summary import page_summary_body
from app_pages.page_eda_ivf_treatment import page_eda_ivf_treatment_body

# Create an instance of the app
app = MultiPage(app_name="IVF Predictor")

app.add_page("Quick Project Summary", page_summary_body)
app.add_page(
    "Exploratory Analysis of IVF Treatment Data",
    page_eda_ivf_treatment_body
    )

app.run()

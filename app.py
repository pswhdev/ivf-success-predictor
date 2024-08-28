import streamlit as st
from app_pages.multipage import MultiPage

# load pages scripts
from app_pages.page_summary import page_summary_body

# Create an instance of the app
app = MultiPage(app_name= "IVF Predictor")

app.add_page("Quick Project Summary", page_summary_body)

app.run()

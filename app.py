import streamlit as st
from app_pages.multipage import MultiPage

# load pages scripts
from app_pages.page_summary import page_summary_body
from app_pages.page_eda_ivf_treatment import page_eda_ivf_treatment_body
from app_pages.page_project_hypotheses import page_project_hypotheses_body
from app_pages.page_ml_success_predictor import page_ml_success_predictor_body
from app_pages.page_live_predictor import page_live_predictor_body

# Create an instance of the app
app = MultiPage(app_name="IVF Success Predictor")

app.add_page("Quick Project Summary", page_summary_body)
app.add_page(
    "Exploratory Analysis of IVF Treatment Data",
    page_eda_ivf_treatment_body
    )
app.add_page("Project Hypotheses", page_project_hypotheses_body)
app.add_page("ML: Predict Success", page_ml_success_predictor_body)
app.add_page("IVF Success Predictor", page_live_predictor_body)

app.run()

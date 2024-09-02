import streamlit as st
import pandas as pd
import joblib
import gzip

# Load IVF treatment data
# @st.cache_data
def load_ifv_treatment_data():
    """Loads the cleaned IVF treatment data from a CSV file."""
    df = pd.read_csv('outputs/datasets/cleaned/FertilityTreatmentDataCleaned.csv')
    return df

# Load a pickle file using joblib
# @st.cache_data
def load_pkl_file(file_path):
    """Loads a pickle file using joblib."""
    return joblib.load(file_path)

# Load a gzip-compressed pickle file using joblib
# @st.cache_data
def load_gzip_file(file_path):
    """Loads a gzip-compressed pickle file using joblib."""
    with gzip.open(file_path, 'rb') as f:
        return joblib.load(f)

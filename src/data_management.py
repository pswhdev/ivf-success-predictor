import streamlit as st
import pandas as pd
import joblib
import gzip



# Load IVF treatment data
@st.cache_data
def load_ifv_treatment_data():
    """Loads the cleaned IVF treatment data from a CSV file."""
    df = pd.read_csv(
        "outputs/datasets/cleaned/FertilityTreatmentDataCleaned.csv"
        )
    return df

@st.cache_data
def load_ifv_treatment_data_before_cleaning():
    """Loads the IVF treatment data from a CSV file before cleaning."""
    df = pd.read_csv(
        "outputs/datasets/collection/FertilityTreatmentData.csv.gz"
        )
    return df

# Load a pickle file using joblib
@st.cache_data
def load_pkl_file(file_path):
    """Loads a pickle file using joblib."""
    return joblib.load(file_path)


# Load a gzip-compressed pickle file using joblib
@st.cache_data
def load_gzip_file(file_path):
    """Loads a gzip-compressed pickle file using joblib."""
    with gzip.open(file_path, "rb") as f:
        return joblib.load(f)


def load_best_features(version="v1"):
    """Load best features from the CSV file saved in the output directory."""
    try:
        best_features_df = pd.read_csv(
            f"outputs/ml_pipeline/ivf_success_predictor/"
            f"{version}/best_features.csv"
        )
        # Convert DataFrame column to a list
        best_features = best_features_df["feature"].tolist()

    except FileNotFoundError:
        st.error(
            """
            Best features file not found. Please ensure it is
            saved correctly in the output folder.
            """
        )
        best_features = []

    return best_features


import streamlit as st
import pandas as pd
from src.data_management import (
    load_ifv_treatment_data,
    load_pkl_file,
    load_gzip_file,
    load_best_features
    )
from src.machine_learning.evaluate_clf import clf_performance

from src.machine_learning.prediction_live import (
    predict_success
    )


def page_live_predictor_body():

    # load files
    version = 'v1'
    ml_pipe_dc_fe = load_pkl_file(
        f"outputs/ml_pipeline/ivf_success_predictor/{version}/"
        "clf_pipeline_data_cleaning_feat_eng.pkl"
    )
    ml_pipe_model = load_gzip_file(
        f"outputs/ml_pipeline/ivf_success_predictor/{version}/"
        "clf_pipeline_model.pkl.gz"
    )
    best_features = load_best_features(version)

    st.write(
        """
        ### IVF Success Predictor - Live Prediction
        """
        )
    st.info(
        """
        This page allows you to predict the success of an IVF treatment
        based on the data you provide.
        """
    )
    st.write("---")

    # Generate Live Data

    # The widgets inputs are the features used in the pipeline for the ML model
    X_live = DrawInputsWidgets()

    # predict on live data
    if st.button("Run Predictive Analysis"):
        success_prediction = predict_success(
            X_live, best_features, ml_pipe_dc_fe, ml_pipe_model)


def DrawInputsWidgets():
    # Load dataset
    df = load_ifv_treatment_data()

    # Get best features
    best_features = load_best_features()

    # Create an empty DataFrame, which will be the live data
    X_live = pd.DataFrame([], index=[0])

    # Dynamically create columns based on the number of best features
    num_features = len(best_features)
    num_cols = min(num_features, 4)  # Adjust the number of columns displayed
    cols = st.columns(num_cols)  # Create columns

    # Iterate over the best features and create widgets
    for i, feature in enumerate(best_features):
        col = cols[i % num_cols]  # Distribute widgets across columns

        # Check if feature is categorical or numerical to decide the widget type
        if pd.api.types.is_numeric_dtype(df[feature]):
            # Numerical input
            st_widget = col.number_input(
                label=feature,
                value=float(df[feature].mean())  # Default to mean or other central value
            )
        else:
            # Categorical input
            st_widget = col.selectbox(
                label=feature,
                options=df[feature].unique(),
                index=0  # Default to the first option
            )
        
        # Assign the input to the DataFrame
        X_live[feature] = st_widget

    return X_live


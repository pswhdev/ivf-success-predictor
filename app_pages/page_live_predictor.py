import streamlit as st
import pandas as pd
from src.data_management import (
    load_ifv_treatment_data,
    load_pkl_file,
    load_gzip_file
    )
# from src.machine_learning.evaluate_clf import clf_performance
# from src.custom_transformers import (
#     FilterIVFTreatments,
#     DropErroneousEntries,
#     ConvertToNumeric,
#     ConvertToIntegers,
#     FillSpermSource,
#     ConvertToIntAndReplace999,
#     ReplaceMissingValues,
#     AppendCycleType,
#     MicroInjectedEmbryos,
#     DonorAgeImputer,
#     FloatToIntTransformer,
#     EFlaggingTransformer,
#     TypeOfCycleAppender,
#     DropRowsWith999,
# )
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
    best_features = (pd.read_csv(
        f"outputs/ml_pipeline/ivf_success_predictor/{version}/X_train.csv")
                      .columns
                      .to_list()
                      )

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

    # load dataset
    df = load_ifv_treatment_data()

# we create input widgets for 11 features
    col1, col2, col3, col4 = st.columns(4)
    col5, col6, col7, col8 = st.columns(4)
    col9, col10, col11, col12 = st.columns(4)

    # We are using these features to feed the ML pipeline
    # values copied from best_features

    # create an empty DataFrame, which will be the live data
    X_live = pd.DataFrame([], index=[0])

    # from here on we draw the widget based on the variable type
    # (categorical or numerical) and set initial values
    with col1:
        feature = "Patient age at treatment"
        st_widget = st.selectbox(
            label=feature,
            options=df[feature].unique()
        )
    X_live[feature] = st_widget

    with col2:
        feature = "Patient/Egg provider age"
        st_widget = st.selectbox(
            label=feature,
            options=df[feature].unique()
        )
    X_live[feature] = st_widget

    with col3:
        feature = "Partner/Sperm provider age"
        st_widget = st.selectbox(
            label=feature,
            options=df[feature].unique()
        )
    X_live[feature] = st_widget

    with col4:
        feature = "Total number of previous IVF cycles"
        st_widget = st.selectbox(
            label=feature,
            options=df[feature].unique()
        )
    X_live[feature] = st_widget

    with col5:
        feature = "Total number of previous pregnancies - IVF and DI"
        st_widget = st.selectbox(
            label=feature,
            options=df[feature].unique()
        )
    X_live[feature] = st_widget

    with col6:
        feature = "Causes of infertility - male factor"
        st_widget = st.selectbox(
            label=feature,
            options=df[feature].unique()
        )
    X_live[feature] = st_widget

    with col7:
        feature = "Fresh eggs collected"
        st_widget = st.selectbox(
            label=feature,
            options=df[feature].unique()
        )
    X_live[feature] = st_widget

    with col8:
        feature = "Total eggs mixed"
        st_widget = st.selectbox(
            label=feature,
            options=df[feature].unique()
        )
    X_live[feature] = st_widget

    with col9:
        feature = "Total embryos created"
        st_widget = st.selectbox(
            label=feature,
            options=df[feature].unique()
        )
    X_live[feature] = st_widget

    with col10:
        feature = "Embryos transferred"
        st_widget = st.selectbox(
            label=feature,
            options=df[feature].unique()
        )
    X_live[feature] = st_widget

    with col11:
        feature = "Date of embryo transfer"
        st_widget = st.selectbox(
            label=feature,
            options=df[feature].unique()
        )
    X_live[feature] = st_widget

    # st.write(X_live)

    return X_live

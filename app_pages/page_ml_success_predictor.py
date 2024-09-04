import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from src.data_management import (
    load_ifv_treatment_data,
    load_pkl_file,
    load_gzip_file
)
from src.machine_learning.evaluate_clf import clf_performance


def page_ml_success_predictor_body():

    version = "v1"
    # load needed files
    ivf_pipe_dc = load_pkl_file(
        f"outputs/ivf_success_predictor/data_cleaning_pipeline/{version}/"
        "data_cleaning_pipeline.pkl"
    )

    ivf_preprocessing = load_pkl_file(
        f"outputs/ml_pipeline/ivf_success_predictor/{version}/"
        "clf_pipeline_pre_processing.pkl"
    )

    ivf_pipe_model = load_gzip_file(
        f"outputs/ml_pipeline/ivf_success_predictor/{version}/"
        "clf_pipeline_model.pkl.gz"
    )

    ivf_feat_importance = plt.imread(
        f"outputs/ml_pipeline/ivf_success_predictor/{version}"
        "/features_importance.png"
    )

    X_train = pd.read_csv(
        f"outputs/ml_pipeline/ivf_success_predictor/{version}/X_train.csv"
    )

    X_test = pd.read_csv(
        f"outputs/ml_pipeline/ivf_success_predictor/{version}/X_test.csv"
    )

    y_train = pd.read_csv(
        f"outputs/ml_pipeline/ivf_success_predictor/{version}/y_train.csv"
    ).values

    y_test = pd.read_csv(
        f"outputs/ml_pipeline/ivf_success_predictor/{version}/y_test.csv"
    ).values

    st.write("### ML Pipeline: IVF Success Predictor")
    # display pipeline training summary conclusions
    st.info(
        """
        * The pipeline was tuned to achieve a mean F1 score of at least 0.7.
        This is crucial because the goal is to minimize the risk of
        providing false hope by predicting treatment success when there
        is a high chance of failure.

        * However, due to the complexity of biological interactions that
        are not fully captured by the dataset, and the low predictive
        power of the variables as indicated by correlation analysis, the ML
        model did not achieve the desired predictive performance. The model's
        mean F1 Score is 0.74 on the training set but drops significantly to
        0.57 on the test set.
        """
    )

    # show pipelines
    st.write("---")
    st.write("#### There are 3 ML Pipelines:")

    st.write(
        """
        The first is responsible for data cleaning and it is shared by all ML
        Models.
        """
    )
    st.write(ivf_pipe_dc)

    st.write(
        """
        The second is carries on further feature engineering tasks.
        """
    )
    st.write(ivf_preprocessing)

    st.write(
        """
        The third one is the modelling pipeline.
        """
    )
    st.write(ivf_pipe_model)

    # show feature importance plot
    st.write("---")
    st.write(
        """
        The features the model was trained and their importance.
        """
    )

    st.write(X_train.columns.to_list())
    st.image(ivf_feat_importance)

    # No need to apply dc_fe pipeline, since X_train and X_test
    # were already transformed in the jupyter notebook
    # (05 - Modeling and Evaluation Predict Success.ipynb)

    # evaluate performance on train and test set
    st.write("---")
    st.write("### Pipeline Performance")
    clf_performance(
        X_train=X_train,
        y_train=y_train,
        X_test=X_test,
        y_test=y_test,
        pipeline=ivf_pipe_model,
        label_map=["No Success", "Success"],
    )

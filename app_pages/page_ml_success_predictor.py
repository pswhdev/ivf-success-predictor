import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from src.data_management import (
    load_ifv_treatment_data,
    load_pkl_file,
    load_gzip_file
    )
from src.machine_learning.evaluate_clf import clf_performance
from src.custom_transformers import (
    FilterIVFTreatments,
    DropErroneousEntries,
    ConvertToNumeric,
    ConvertToIntegers,
    FillSpermSource,
    ConvertToIntAndReplace999,
    ReplaceMissingValues,
    AppendCycleType,
    MicroInjectedEmbryos,
    DonorAgeImputer,
    FloatToIntTransformer,
    EFlaggingTransformer,
    TypeOfCycleAppender,
    DropRowsWith999,
)


def page_ml_success_predictor_body():

    version = "v1"
    # load needed files
    ivf_pipe_dc_fe = load_pkl_file(
        f"outputs/ml_pipeline/ivf_success_predictor/{version}/"
        "clf_pipeline_data_cleaning_feat_eng.pkl"
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
        * The pipeline was tuned aiming at least 0.70 Precision on F1 Score
        for Success, since we are interested in this project in predicting
        chances of IVF Treatment success.

        * The pipeline performance on train and test set is 0.79 and 0.49,
        respectively.
        """
    )

    # show pipelines
    st.write("---")
    st.write("#### There are 2 ML Pipelines arranged in series.")

    st.write(
        """
        * The first is responsible for data cleaning and feature engineering.
        """
    )
    st.write(ivf_pipe_dc_fe)

    st.write(
        """
        * The second is for feature scaling and modelling.
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

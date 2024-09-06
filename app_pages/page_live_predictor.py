import streamlit as st
import pandas as pd
from src.data_management import (
    load_ifv_treatment_data,
    load_pkl_file,
    load_gzip_file,
    load_best_features,
    load_ifv_treatment_data_before_cleaning
)
from src.machine_learning.prediction_live import (
    predict_success,
)


def page_live_predictor_body():
    """
    The main function that sets up the Streamlit page for live prediction
    of IVF success.
    It loads the necessary models, displays the user input widgets, and
    triggers the prediction process.
    """

    # Load necessary files and models
    # Define the version of the model to use
    version = "v1"

    # Loads the pre-processing pipeline (feature engineering steps)
    ml_pipe_fe = load_pkl_file(
        f"outputs/ml_pipeline/ivf_success_predictor/{version}/"
        "clf_pipeline_pre_processing.pkl"
    )
    # Loads the trained classification model in gzipped format
    ml_pipe_model = load_gzip_file(
        f"outputs/ml_pipeline/ivf_success_predictor/{version}/"
        "clf_pipeline_model.pkl.gz"
    )
    # Loads the list of best features used by the model
    best_features = load_best_features(version)

    # Display the title and description using Streamlit
    st.write(
        """
        ### Live Prediction
        """
    )
    st.info(
        """
        Welcome to the **Hope Fertility Clinic IVF Success Predictor**.
        
        This dashboard is designed for our staff to assess the likelihood
        of IVF treatment success based on patient-specific data.
        Please enter the data and click on the button to run the predictive
        analysis.
        """
    )
    st.write("---")

    # Generate Live Data from user inputs
    # This function creates input widgets corresponding to the features
    # used in the ML model
    X_live = DrawInputsWidgets()

    # Button to run the prediction analysis; on click,
    # triggers the prediction process
    if st.button("Run Predictive Analysis"):
        # Call the predict_success function using the live input data,
        # selected features, and loaded models
        success_prediction = predict_success(
            X_live, best_features, ml_pipe_fe, ml_pipe_model
        )


def DrawInputsWidgets():
    """
    Creates input widgets on the Streamlit page for each feature required
    by the model using the available data to provide user-friendly inputs
    for each feature.
    """

    # Load the IVF treatment data into a DataFrame for reference
    df = load_ifv_treatment_data()

    # Load the selected best features for the model
    best_features = load_best_features()

    # Initialize an empty DataFrame with columns matching the best features
    # Creates an empty DataFrame with specified columns (Pandas API)
    X_live = pd.DataFrame(columns=best_features)
    # Create a layout with columns to arrange the input widgets neatly
    # Determine the number of features to display
    num_features = len(best_features)
    # Display up to 4 columns of widgets at a time
    num_cols = min(num_features, 4)
    # Creates the specified number of columns in the layout
    cols = st.columns(num_cols)

    # Flags to control the display of additional information
    embryos_transferred_info_displayed = False
    cycle_info_displayed = False

    # Iterate over each feature to create an appropriate input widget
    for i, feature in enumerate(best_features):
        # Selects the column to place the widget in (cycle among the available
        # columns ensuring that widgets are distributed evenly across the
        # available columns, wrapping around when the end of the column list
        # is reached
        col = cols[i % num_cols]

        # Display specific information about the "Embryos transferred" feature
        # if not already displayed
        if (
            feature == "Embryos transferred"
            and not embryos_transferred_info_displayed
        ):
            st.write("* 1e means 1 embryo selectively elected.")
            embryos_transferred_info_displayed = True

        # Display additional info about cycle type
        if (
            not pd.api.types.is_numeric_dtype(df[feature])
            and not cycle_info_displayed):
            # Checks if the feature contains information about frozen
            # or fresh cycles
            if any(
                "- frozen" in str(val) or "- fresh" in str(val)
                for val in df[feature].unique()
            ):
                # Explanation of the frozen/fresh cycle information
                st.write(
                    """
                    * '- frozen' or '- fresh' indicates frozen or
                    fresh cycle, respectively.
                    """
                )
                cycle_info_displayed = True

        # Create appropriate input widgets based on the data type
        # of the feature using Pandas API
        if pd.api.types.is_numeric_dtype(df[feature]):
            # Extracts unique values of the feature using Pandas API
            unique_values = df[feature].unique()
            # Checks if the feature is binary (0/1)
            if set(unique_values) == {0, 1}:
                # Create a dropdown for binary features (Yes/No)
                st_widget = col.selectbox(
                    # Label for the dropdown
                    label=feature,
                    # Options presented to the user
                    options=["No", "Yes"],
                    # Default selection index
                    index=0,
                )
                # Assigns 1 or 0 based on user input (Pandas API)
                X_live.at[0, feature] = 1 if st_widget == "Yes" else 0
            else:
                # Create a number input for continuous or discrete
                # numeric features
                min_value = int(
                    # Minimum value of the feature (Pandas API)
                    df[feature].min()
                )
                max_value = int(
                    # Maximum value of the feature (Pandas API)
                    df[feature].max()
                )
                st_widget = col.number_input(
                    label=feature,
                    value=int(
                        # Default value set to the mean of the feature
                        # (Pandas API)
                        df[feature].mean()
                    ),
                    # Increment or decrement step size (1 numer at a time)
                    step=1,
                    # Format the input as an integer
                    format="%d",
                    min_value=min_value,
                    max_value=max_value,
                )
                # Assigns the user's input to the DataFrame (Pandas API)
                X_live.at[0, feature] = st_widget
        else:
            # For categorical features, create a dropdown with sorted options
            sorted_options = sorted(
                df[feature].unique()
            )  # Sorts unique values of the feature (Pandas API)
            st_widget = col.selectbox(
                label=feature,
                # Options presented to the user
                options=sorted_options,
                index=0,
            )
            X_live.at[0, feature] = st_widget

    # Check if the input DataFrame is empty or not populated
    # Checks if the DataFrame is empty (Pandas API)
    if X_live.empty:
        st.error(
            """
            No input data has been provided.
            Please fill in all required fields.
            """
        )
        return None

    # Return the populated DataFrame with live input data
    return X_live

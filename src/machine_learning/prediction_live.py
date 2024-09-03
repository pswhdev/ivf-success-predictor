import streamlit as st


def predict_success(X_live, best_features, ml_pipe_dc_fe, ml_pipe_model):
    # Subset live data to match the features used in the pipeline
    expected_features = ml_pipe_dc_fe.feature_names_in_  # Expected features used during training
    X_live_ivf = X_live.filter(expected_features, axis=1)  # Filter and reorder to match expected features

    # Check if any feature is missing and add it with a default value (e.g., mean or most frequent)
    missing_features = set(expected_features) - set(X_live_ivf.columns)
    for feature in missing_features:
        # Adding missing features with a default value (adjust based on feature type if needed)
        X_live_ivf[feature] = 0  # You may need to adjust this to a reasonable default value

    # Apply the data cleaning and feature engineering pipeline to live data
    X_live_ivf_dc_fe = ml_pipe_dc_fe.transform(X_live_ivf)

    # Predict
    success_prediction = ml_pipe_model.predict(X_live_ivf_dc_fe)
    success_prediction_proba = ml_pipe_model.predict_proba(X_live_ivf_dc_fe)

    # Create a logic to display the results
    success_prob = success_prediction_proba[0, success_prediction][0] * 100
    if success_prediction == 1:
        success_result = 'will'
    else:
        success_result = 'will not'

    statement = (
        f'### There is {success_prob.round(1)}% probability '
        f'that the treatment **{success_result} be successful**.'
    )

    st.write(statement)
    return success_prediction


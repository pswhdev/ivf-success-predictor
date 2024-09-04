import streamlit as st

def predict_success(X_live, best_features, ml_pipe_dc_fe, ml_pipe_model):
    # Get the expected columns from the transformer
    expected_columns = ml_pipe_dc_fe.feature_names_in_

    # Ensure X_live_ivf contains all expected columns, filling missing
    # ones with 0
    X_live_ivf = X_live.reindex(columns=expected_columns, fill_value=0)

    # Apply data cleaning/feature engineering pipeline to the live data
    try:
        X_live_ivf_dc_fe = ml_pipe_dc_fe.transform(X_live_ivf)
    except ValueError as e:
        st.error(f"Transformation error: {e}")
        return None

    # Subset the transformed data to best features before prediction
    X_live_ivf_dc_fe_best = X_live_ivf_dc_fe[best_features]

    # Predict using the model
    success_prediction = ml_pipe_model.predict(X_live_ivf_dc_fe_best)
    success_prediction_proba = ml_pipe_model.predict_proba(
        X_live_ivf_dc_fe_best
        )

    # Calculate success probability
    success_prob = success_prediction_proba[0, success_prediction][0] * 100
    success_result = 'will' if success_prediction == 1 else 'will not'

    # Display results
    statement = (
        f'### There is {success_prob.round(1)}% probability '
        f'that the treatment **{success_result} be successful**.'
    )
    st.write(statement)

    return success_prediction

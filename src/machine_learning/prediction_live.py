import streamlit as st


def predict_success(X_live, best_features, ml_pipe_dc_fe, ml_pipe_model):

    # from live data, subset features related to this pipeline
    X_live_ivf = X_live.filter(best_features)

    # apply data cleaning / feat engine pipeline to live data
    X_live_ivf_dc_fe = ml_pipe_dc_fe.transform(X_live_ivf)

    # predict
    success_prediction = ml_pipe_model.predict(X_live_ivf_dc_fe)
    success_prediction_proba = ml_pipe_model.predict_proba(
        X_live_ivf_dc_fe)
    # st.write(success_prediction_proba)

    # Create a logic to display the results
    success_prob = success_prediction_proba[0, success_prediction][0]*100
    if success_prediction == 1:
        success_result = 'will'
    else:
        success_result = 'will not'

    statement = (
        f'### There is {success_prob.round(1)}% probability '
        f'that the treatment **{success_result} be successful**.')

    st.write(statement)

    return success_prediction

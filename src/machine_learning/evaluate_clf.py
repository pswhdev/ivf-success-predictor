import streamlit as st
import pandas as pd
from sklearn.metrics import classification_report, confusion_matrix


# Modified function for confusion matrix and report
def confusion_matrix_and_report(X, y, pipeline, label_map):
    prediction = pipeline.predict(X)

    st.write("#### Confusion Matrix")
    # Adjust to take more space by wrapping the table in a container
    # with 'use_container_width=True'
    st.table(
        pd.DataFrame(
            confusion_matrix(y_true=prediction, y_pred=y),
            columns=["Actual " + sub for sub in label_map],
            index=["Prediction " + sub for sub in label_map],
        )
    )

    st.write("#### Classification Report")
    # Generate classification report as a dictionary, convert to DataFrame,
    # and round values
    report_dict = classification_report(
        y, prediction, target_names=label_map,
        output_dict=True
    )
    report_df = pd.DataFrame(report_dict).transpose()
    report_df = report_df.round(2)  # Round values to 2 decimals

    # Display with more space, using 'use_container_width=True'
    # for wider display
    st.dataframe(report_df, use_container_width=True)


def clf_performance(X_train, y_train, X_test, y_test, pipeline, label_map):
    st.info("Train Set")
    confusion_matrix_and_report(X_train, y_train, pipeline, label_map)

    st.info("Test Set")
    confusion_matrix_and_report(X_test, y_test, pipeline, label_map)

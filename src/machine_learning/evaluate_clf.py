import streamlit as st
import pandas as pd
from sklearn.metrics import classification_report, confusion_matrix


def confusion_matrix_and_report(X, y, pipeline, label_map, display=True):
    """
    Display the confusion matrix and classification report for model predictions, 
    and return the mean F1 score.

    Parameters:
    - X: Features for evaluation.
    - y: True labels.
    - pipeline: The trained ML pipeline used for predictions.
    - label_map: A list mapping label indices to label names.
    - display: Boolean flag to control whether to display the matrix and report.

    Returns:
    - mean_f1_score: The mean F1 score for the evaluated set.
    """
    # Generate predictions
    prediction = pipeline.predict(X)

    if display:
        # Display the confusion matrix
        st.write("#### Confusion Matrix")
        st.table(
            pd.DataFrame(
                confusion_matrix(y_true=y, y_pred=prediction),
                columns=["Actual " + sub for sub in label_map],
                index=["Prediction " + sub for sub in label_map],
            )
        )

        # Generate classification report as a dictionary
        st.write("#### Classification Report")
        report_dict = classification_report(
            y, prediction, target_names=label_map, output_dict=True
        )
        report_df = pd.DataFrame(report_dict).transpose().round(2)
        st.dataframe(report_df, use_container_width=True)
    else:
        # Generate classification report as a dictionary without displaying
        report_dict = classification_report(
            y, prediction, target_names=label_map, output_dict=True
        )

    # Extract F1 scores for both classes (Success and No Success)
    f1_success = report_dict.get('Success', {}).get('f1-score', 0)
    f1_no_success = report_dict.get('No Success', {}).get('f1-score', 0)

    # Calculate the mean F1 score for the evaluated set
    mean_f1_score = (f1_success + f1_no_success) / 2

    st.write(f"Mean F1 score: {mean_f1_score:.2f}")

    # Return the mean F1 score
    return mean_f1_score


def clf_performance(X_train, y_train, X_test, y_test, pipeline, label_map):
    """
    Display performance metrics for training and test sets and calculate mean
    F1 scores.
    """
    # Get mean F1 score for the training set without displaying
    mean_f1_train = confusion_matrix_and_report(X_train, y_train, pipeline, label_map, display=True)

    # Get mean F1 score for the test set without displaying
    mean_f1_test = confusion_matrix_and_report(X_test, y_test, pipeline, label_map, display=True)

    # Return the mean F1 scores
    return mean_f1_train, mean_f1_test

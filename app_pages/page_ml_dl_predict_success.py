import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from src.data_management import load_ifv_treatment_data, load_pkl_file
from src.machine_learning.evaluate_clf import load_test_evaluation

def page_ml_dl_predict_success_body():

    version = 'v1'
import streamlit as st
import plotly.express as px
import numpy as np
from src.data_management import load_ifv_treatment_data
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import seaborn as sns

sns.set_style("whitegrid")


def page_project_hypotheses_body():

    # Load data using the cached function
    df = load_ifv_treatment_data()

    vars_to_study = [
        "Patient age at treatment",
        "Patient/Egg provider age",
        "Elective single embryo transfer",
        "Embryos transferred",
        "Causes of infertility - endometriosis",
        "Partner/Sperm provider age",
    ]

        
    st.markdown(
        """
        ### Project Hypotheses and Validation
        """
    )

    st.success(
        """
        1. Patient age has a direct impact on the success rate of IVF
        treatments.
            - The data strongly supports the hypothesis that patient age
            directly impacts IVF success rates. Younger patients,
            particularly those under 35, have notably higher success
            rates compared to older patients, confirming that age is a
            critical factor in IVF treatment outcomes. The increase of
            success rate for older patients can be explained by the
            fact that the treatment was carried out with donor eggs.

        2. Elective single embryo transfer (eSET) reduces the likelihood
        of multiple pregnancies without significantly lowering the overall
        success rate.
            - The data indicates that elective single embryo transfers are
            highly represented in successful outcomes, showing to be an
            effective strategy in reducing the risk of multiple pregnancies
            while maintaining success rate.

        3. Patients with a history of endometriosis have lower IVF success
        rates compared to those without endometriosis.
            - The pie chart indicates that six percent of successful cases
            involve patients with endometriosis, and ninety four percent
            involve those without. This may seem to suggest lower success
            among endometriosis patients, but this comparison does not account
            for the prevalence of endometriosis in the overall patient
            population. Further analysis shows that only a small proportion
            of patients have endometriosis, and the success rates for these
            patients are comparable to those without the condition (see stacked
            bar plot). This suggests that endometriosis does not significantly
            impact IVF.
            - As a result, the data does not provide strong evidence that
            endometriosis leads to significantly lower IVF success rates.

        4. The age of the semen provider does not influence the success rate
        of IVF treatments.
            - Although the pie chart shows that the largest proportion of
            successful IVF cases involve sperm providers aged 18-34, followed
            by 35-37, and progressively smaller proportions in older age
            groups, it does not take into account the distribution of
            sperm provider ages in the overall patient population.
            - The stacked bar chart shows that the success rates reduce
            slightly with increasing sperm provider age, but the differences
            are not substantial. This suggests that the age of the sperm
            provider does not significantly influence IVF success rates.

        """
    )

# Create a filtered DataFrame based on vars_to_study
    df_eda = df.filter(vars_to_study + ["Live birth occurrence"])
    
    # Checkbox to display the radio buttons for data visualization
    if st.checkbox("Visualize Data"):
        # Select a variable for exploration
        selected_variable = st.radio("Select a variable to explore:", vars_to_study, index=0)
        # Display plots based on selected variable
        st.write(f"### Plots for: {selected_variable}")
        display_selected_plots(df_eda, selected_variable, "Live birth occurrence")

def display_selected_plots(df, col, target_var):
    """Displays count, proportion, and pie charts based on the selected column."""
    # Count distribution plot
    st.write(f"**Count Distribution for {col}**")
    plot_count_distribution(df, col, target_var)

    # Proportional distribution plot
    st.write(f"**Proportional Distribution for {col}**")
    plot_proportion_distribution(df, col, target_var)

    # Pie chart
    st.write(f"**Pie Chart for {col}**")
    plot_pie_chart(df, col, target_var)

def plot_count_distribution(df, col, target_var):
    plt.figure(figsize=(15, 6))

    order = sorted(
        # Sort other categorical columns in ascending order as strings
        df[col].unique(),
        key=str,
    )

    sns.countplot(data=df, x=col, hue=target_var, order=order)
    plt.xticks(rotation=90)
    plt.title(f"{col}", fontsize=20, y=1.05)
    plt.ylabel(f"Number of Cases")
    st.pyplot(plt.gcf())


# Function to plot proportional distributions
def plot_proportion_distribution(df, col, target_var):
    plt.figure(figsize=(15, 6))

    order = sorted(
        df[col].unique(), key=str
    )  # Sort other categorical columns in ascending order as strings

    # Filter order to match only existing categories
    unique_values = df[col].unique()
    order = [x for x in order if x in unique_values]

    # Calculate proportions
    df_prop = df.groupby([col, target_var]).size().reset_index(name="count")
    df_prop["proportion"] = df_prop.groupby(col)["count"].transform(
        lambda x: x / x.sum()
    )

    # Pivot the data to have proportions for each target
    # variable as separate columns
    df_pivot = df_prop.pivot(index=col, columns=target_var, values="proportion").fillna(
        0
    )
    df_pivot = df_pivot.reindex(
        # Reorder according to the predefined order
        order, fill_value=0
    )  

    # Plot using Matplotlib to stack bars
    if not df_pivot.empty:
        plt.bar(
            df_pivot.index,
            df_pivot[0],
            label="Live birth occurrence 0",
            color="#3274a1",
        )
        if 1 in df_pivot.columns:
            plt.bar(
                df_pivot.index,
                df_pivot[1],
                bottom=df_pivot[0],
                label="Live birth occurrence 1",
                color="#e1812c",
            )

    # Format y-axis as percentages
    plt.gca().yaxis.set_major_formatter(mtick.PercentFormatter(1.0))
    plt.xticks(rotation=90)
    plt.title(f"Proportional Distribution of {col} by {target_var}", fontsize=20, y=1.05)
    plt.ylabel(f"Proportional Percentage of Outcomes by {col}")
    plt.xlabel(col)
    plt.legend(title=target_var, loc="upper right")

    # Add labels to the stacked bars
    for i in range(len(df_pivot)):
        if (
            0 in df_pivot.columns
            and np.isfinite(df_pivot.iloc[i, 0])
            and df_pivot.iloc[i, 0] > 0
        ):
            plt.text(
                i,
                df_pivot.iloc[i, 0] / 2,
                f"{df_pivot.iloc[i, 0]:.1%}",
                ha="center",
                va="center",
                color="white",
                fontsize=9,
            )
        if (
            1 in df_pivot.columns
            and np.isfinite(df_pivot.iloc[i, 1])
            and df_pivot.iloc[i, 1] > 0
        ):
            plt.text(
                i,
                df_pivot.iloc[i, 0] + df_pivot.iloc[i, 1] / 2,
                f"{df_pivot.iloc[i, 1]:.1%}",
                ha="center",
                va="center",
                color="black",
                fontsize=9,
            )

    st.pyplot(plt.gcf())


# Choose color palette
palette = sns.color_palette("colorblind")


# Function to plot pie charts
def plot_pie_chart(df, col, target_var):
    # Filter the data to include only successful cases
    df_successful = df[df[target_var] == 1]

    # Aggregate counts within each category for successful cases
    df_pie = df_successful.groupby([col]).size().reset_index(name="count")

    # Calculate total count for percentage calculations
    total_count = df_pie["count"].sum()

    # Calculate the percentage for each slice
    df_pie["percentage"] = df_pie["count"] / total_count

    # Define threshold for displaying labels directly on the pie chart
    threshold = 0.05  # 5%

    # Creating labels for the legend with counts and percentages
    legend_labels = [
        f"{label}: {count} ({count/total_count:.1%})"
        for label, count in zip(df_pie[col], df_pie["count"])
    ]
    # Check the number of categories
    if len(df_pie) == 2:
        colors = ["#019e73", "#cb78bc"]
    else:
        colors = palette
    # Plot pie chart for successful cases
    plt.figure(figsize=(15, 6)) 
    wedges, texts, autotexts = plt.pie(
        df_pie["count"],
        startangle=90,
        colors=colors,
        labels=[
            label if pct > threshold else "" for label, pct in zip(df_pie[col], df_pie["percentage"])
        ],
        autopct=lambda p: f"{p:.1f}%" if p / 100 > threshold else "",
    )

    # Adjust the text color on the pie chart
    for text in autotexts:
        text.set_color("black")

    # Move the legend to the right outside the plot area
    plt.legend(
        wedges,
        legend_labels,
        title=col,
        loc="center left",
        # Move the legend outside the plot area
        bbox_to_anchor=(1.05, 0.5)
    )

    plt.title(f"Distribution of {col} in Successful IVF Cases", fontsize=20, y=1.05)
    st.pyplot(plt.gcf())
import plotly.express as px
import numpy as np
import streamlit as st
from src.data_management import load_ifv_treatment_data
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import seaborn as sns

sns.set_style("whitegrid")


def page_eda_ivf_treatment_body():
    # Load data using the cached function
    df = load_ifv_treatment_data()

    vars_to_study = [
        "Date of embryo transfer",
        "Elective single embryo transfer",
        "Embryos transferred",
        "Fresh eggs collected",
        "Total eggs mixed",
        "Total embryos created",
        "Patient/Egg provider age",
        "Partner/Sperm provider age",
        "Causes of infertility - endometriosis",
    ]

    st.write("### Exploratory Analysis of IVF Treatment Data")
    st.info(
        """
        Welcome to the Exploratory Analysis of IVF Treatment Data, developed
        for Hope Fertility Clinic. This dashboard highlights key factors
        influencing IVF success rates through detailed data visualizations,
        revealing relationships between clinical variables and treatment
        outcomes.

        Factors such as embryo transfer timing, number of embryos transferred,
        and patient demographics are analyzed to support data-driven decisions,
        enhancing understanding and improving treatment strategies.
        """
    )

    # Inspect data
    if st.checkbox("Inspect dataset"):
        st.write(
            f"The dataset has {df.shape[0]} rows and {df.shape[1]} columns",
            f"find below the first 10 rows.",
        )
        st.write(df.head(10))

    st.write("---")

    # Correlation Study Summary
    st.write(
        f"A correlation study was conducted to better understand"
        f"how the variables are correlated with successful treatment outcomes."
        f"The most correlated variables are: **{vars_to_study}**."
    )

    st.info(
        """
        The correlation indications and plots below interpretation converge.
        Successful IVF treatment outcomes typically:

        * had the embryo being transferred on day 5 in a fresh cycle or from a
        frozen cycle being transferred on the day they were thawed, day 0.
        * had only one embryo selected electively transferred or 2 embryos
        without elective selection.
        * had more than 5 fresh eggs collected from patient/egg donor or were
        from a frozen cycle.
        * had more than 5 eggs mixed with sperm.
        * had a range of 6-10 embryos created.
        * happened when the Patient/Egg provider was younger than 34 years old.
        * happened when the Partner/Sperm provider was younger than 34 years
        old.
        """
    )

    # Create a filtered DataFrame based on vars_to_study
    df_eda = df.filter(vars_to_study + ["Live birth occurrence"])

    # Convert columns to string to avoid mixed type issues
    columns_to_convert = ["Total embryos created"]
    convert_to_string(df_eda, columns_to_convert)

    # Select a variable for exploration
    selected_variable = st.radio(
        "Select a variable to explore:", vars_to_study, index=0
    )

    # Display plots based on selected variable
    if selected_variable:
        st.write(f"### Plots for: {selected_variable}")
        display_selected_plots(df_eda, selected_variable, "Live birth occurrence")
    # Parallel plot section
    if st.checkbox("Parallel Plot"):
        st.write(
            """
            Information in yellow shows that the treatment was successful.
            """
        )
        # Convert the categorical column to a numeric type
        df_eda['Live birth occurrence'] = df_eda['Live birth occurrence'].astype('category').cat.codes

        # Create the parallel categories plot
        fig = px.parallel_categories(df_eda, color="Live birth occurrence")

        # Update layout to adjust size, font size and margins
        fig.update_layout(
            font=dict(size=8),
            margin=dict(l=50, r=50, t=50, b=50),
            width=1000, height=600
        )

        # Display the plot in Streamlit
        st.plotly_chart(fig)


def display_selected_plots(df, col, target_var):
    """Displays count, proportion, and pie charts based on the selected column."""
    # Count distribution plot
    st.write(f"**Count Distribution for {col}**")
    plot_count_distribution(df, col, target_var)

    # Proportion distribution plot
    st.write(f"**Proportion Distribution for {col}**")
    plot_proportion_distribution(df, col, target_var)

    # Pie chart
    st.write(f"**Pie Chart for {col}**")
    plot_pie_chart(df, col, target_var)


def convert_to_string(df, columns):
    for col in columns:
        # Convert to string to avoid mixed type issues
        df[col] = df[col].astype(str)


def plot_count_distribution(df, col, target_var):
    plt.figure(figsize=(12, 5))

    # Define custom ordering for specific columns with ranges
    if col == "Date of embryo transfer":
        order = [
            "0 - fresh",
            "1 - fresh",
            "2 - fresh",
            "3 - fresh",
            "4 - fresh",
            "5 - fresh",
            "6 - fresh",
            "7 - fresh",
            "0 - frozen",
            "1 - frozen",
            "2 - frozen",
            "3 - frozen",
            "4 - frozen",
            "5 - frozen",
            "6 - frozen",
            "7 - frozen",
            "2 - Mixed fresh/frozen",
            "3 - Mixed fresh/frozen",
            "5 - Mixed fresh/frozen",
            "6 - Mixed fresh/frozen",
            "Missing",
            "NT",
        ]
    elif col in ["Fresh eggs collected", "Total eggs mixed"]:
        order = [
            "0",
            "1-5",
            "6-10",
            "11-15",
            "16-20",
            "21-25",
            "26-30",
            "31-35",
            "36-40",
            ">40",
            "0 - frozen cycle",
        ]
    elif col == "Total embryos created":
        order = [
            "0",
            "1-5",
            "6-10",
            "11-15",
            "16-20",
            "21-25",
            "26-30",
            ">30",
            "0 - frozen cycle",
        ]
    else:
        order = sorted(
            # Sort other categorical columns in ascending order as strings
            df[col].unique(), key=str
        )  

    sns.countplot(data=df, x=col, hue=target_var, order=order)
    plt.xticks(rotation=90)
    plt.title(f"{col}", fontsize=20, y=1.05)
    st.pyplot(plt.gcf())


# Function to plot proportion distributions
def plot_proportion_distribution(df, col, target_var):
    plt.figure(figsize=(15, 6))

    # Define the order specifically for the variable of interest
    if col == "Date of embryo transfer":
        order = [
            "0 - fresh",
            "1 - fresh",
            "2 - fresh",
            "3 - fresh",
            "4 - fresh",
            "5 - fresh",
            "6 - fresh",
            "7 - fresh",
            "0 - frozen",
            "1 - frozen",
            "2 - frozen",
            "3 - frozen",
            "4 - frozen",
            "5 - frozen",
            "6 - frozen",
            "7 - frozen",
            "2 - Mixed fresh/frozen",
            "3 - Mixed fresh/frozen",
            "5 - Mixed fresh/frozen",
            "6 - Mixed fresh/frozen",
            "Missing",
            "NT",
        ]
    elif col in ["Fresh eggs collected", "Total eggs mixed"]:
        order = [
            "0",
            "1-5",
            "6-10",
            "11-15",
            "16-20",
            "21-25",
            "26-30",
            "31-35",
            "36-40",
            ">40",
            "0 - frozen cycle",
        ]
    elif col == "Total embryos created":
        order = [
            "0",
            "1-5",
            "6-10",
            "11-15",
            "16-20",
            "21-25",
            "26-30",
            ">30",
            "0 - frozen cycle",
        ]
    else:
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

    # Pivot the data to have proportions for each target variable as separate columns
    df_pivot = df_prop.pivot(index=col, columns=target_var, values="proportion").fillna(
        0
    )
    df_pivot = df_pivot.reindex(
        order, fill_value=0
    )  # Reorder according to the predefined order

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
    plt.title(f"Proportion Distribution of {col} by {target_var}", fontsize=20, y=1.05)
    plt.ylabel("Proportion")
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

    # Plot pie chart for successful cases
    plt.figure(figsize=(8, 8))
    wedges, texts, autotexts = plt.pie(
        df_pie["count"],
        startangle=90,
        colors=palette,
        labels=[
            # Display category name if above threshold
            label if pct > threshold else ""
            for label, pct in zip(df_pie[col], df_pie["percentage"])
        ],  
        autopct=lambda p: (
            # Show % only if > threshold
            f"{p:.1f}%" if p / 100 > threshold else ""
        ),  
    )

    # Adjust the display of labels on the pie chart
    for text in autotexts:
        text.set_color("black")

    # Adding the legend
    plt.legend(
        wedges, legend_labels, title=col, loc="center left", bbox_to_anchor=(1, 0.5)
    )
    plt.title(f"Distribution of Successful Cases for {col}")
    st.pyplot(plt.gcf())






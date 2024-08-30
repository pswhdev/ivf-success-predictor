import plotly.express as px
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
from src.data_management import load_ifv_treatment_data


sns.set_style("whitegrid")


def page_eda_ivf_treatment_body():
    # Load data using the cached function
    df = load_ifv_treatment_data()

    to_plot = [
        "Date of embryo transfer",
        "Elective single embryo transfer",
        "Embryos transferred",
        "Fresh eggs collected",
        "Total eggs mixed",
        "Total embryos created",
        "Patient/Egg provider age",
        "Partner/Sperm provider age",
        "Parallel Plot",
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

    # Inspect dataset
    if st.checkbox("Inspect dataset"):
        st.write(
            f"The dataset has {df.shape[0]} rows and {df.shape[1]} columns,"
            f"find below the first 10 rows."
        )
        st.write(df.head(10))

    st.write("---")

    # Correlation Study Summary
    st.write(
        """A correlation study was conducted to better understand
        how the variables are correlated with successful treatment outcomes.
        """
    )
    st.write(
        """
        The most correlated variables are: Date of embryo transfer,
        Elective single embryo transfer, Embryos transferred,
        Fresh eggs collected, Total eggs mixed, Total embryos created,
        Patient/Egg provider age, Partner/Sperm provider age.
        """
    )

    st.info(
        """
        The findings from the correlation analysis and data visualization
        suggest key factors that are commonly associated with successful
        IVF treatment outcomes:

        - Embryo transfers performed on day 5 of a fresh cycle or on day 0 of
        a frozen cycle (the day they were thawed) were more likely to result
        in success.
        - Success was often observed when a single embryo was electively
        transferred or when two embryos were transferred without elective
        selection.
        - Collecting more than 5 fresh eggs from the patient or egg donor, or
        utilizing eggs from a frozen cycle, was linked to higher success rates.
        - Mixing more than 5 eggs with sperm was a common factor in successful
        outcomes.
        - Successful treatments typically involved the creation of 6 to 10
        embryos.
        - Higher success rates were noted when the Patient/Egg provider was
        younger than 34 years old.
        - Outcomes were more favorable when the Partner/Sperm provider was
        also younger than 34 years old.
        """
    )

    # Inspect data

    # Create a filtered DataFrame based on to_plot
    # Exclude "Parallel Plot" from filtering columns
    df_eda = df.filter(to_plot[:-1] + ["Live birth occurrence"])
    # Convert columns to string to avoid mixed type issues
    columns_to_convert = ["Total embryos created"]
    convert_to_string(df_eda, columns_to_convert)

    # Checkbox to display the radio buttons for data visualization
    if st.checkbox("Visualize Data"):
        # Select a variable for exploration
        selected_variable = st.radio("Select a variable to explore:", to_plot,
                                     index=0)
        # Display plots based on selected variable or Parallel Plot
        if selected_variable == "Parallel Plot":
            display_parallel_plot(df_eda)
        else:
            st.write(f"### Plots for: {selected_variable}")
            display_selected_plots(df_eda, selected_variable,
                                   "Live birth occurrence")


def display_parallel_plot(df):
    """Displays the parallel categories plot."""
    st.write(
        """
        * Information in yellow shows that the treatment was successful.
        """
    )
    # Convert the categorical column to a numeric type
    df['Live birth occurrence'] = df['Live birth occurrence'].astype('category').cat.codes

    # Create the parallel categories plot with the Viridis color scale
    fig = px.parallel_categories(
        df,
        color="Live birth occurrence",
        color_continuous_scale="Viridis",  
        labels={"Live birth occurrence": "Live Birth Occurrence"},
    )

    # Update layout to adjust size, font size, margins, and background colors
    fig.update_layout(
        title="Parallel Categories Plot of Treatment Outcomes",
        font=dict(size=10, color='black'),
        margin=dict(l=50, r=50, t=70, b=50),
        width=1000, height=600,
        plot_bgcolor='white',  
        paper_bgcolor='white'  
    )

    # Update the colorbar settings to ensure legend text is black
    fig.update_coloraxes(
        colorbar=dict(tickfont=dict(color='black'),
                      titlefont=dict(color='black'))
    )

    # Display the plot in Streamlit
    st.plotly_chart(fig)


def display_selected_plots(df, col, target_var):
    """
    Displays count, proportion, and pie charts based on the selected column.
    """
    # Count distribution plot
    st.write(f"**Count Distribution for {col}**")
    plot_count_distribution(df, col, target_var)

    # Pie chart
    st.write(f"**Pie Chart for {col}**")
    plot_pie_chart(df, col, target_var)


def convert_to_string(df, columns):
    for col in columns:
        # Convert to string to avoid mixed type issues
        df[col] = df[col].astype(str)


def plot_count_distribution(df, col, target_var):
    plt.figure(figsize=(15, 6))

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
            df[col].unique(),
            key=str,
        )

    sns.countplot(data=df, x=col, hue=target_var, order=order)
    plt.xticks(rotation=90)
    plt.title(f"{col}", fontsize=20, y=1.05)
    plt.ylabel(f"Number of Cases")
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
            label if pct > threshold else "" for label, pct in zip(
                df_pie[col],
                df_pie["percentage"]
                )
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

    plt.title(f"Distribution of {col} in Successful IVF Cases",
              fontsize=20, y=1.05)
    st.pyplot(plt.gcf())

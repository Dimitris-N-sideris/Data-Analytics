import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv("medical_examination.csv")
# Add 'overweight' column
df["overweight"] = df["weight"].div(df["height"].div(100).pow(2))
df["overweight"] = (df["overweight"] > 25).astype(int)

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
df["gluc"] = (df["gluc"] > 1).astype(int)
df["cholesterol"] = (df["cholesterol"] > 1).astype(int)

# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
    value_vars = ["active", "alco", "cholesterol", "gluc", "overweight", "smoke"]
    df_cat = pd.melt(df, id_vars=["cardio"], value_vars=value_vars)
    ax = sns.catplot(
        x="variable",
        data=df_cat,
        kind="count",
        col="cardio",
        hue="value",
    )
    ax.set_axis_labels("variable", "total")
    ax.fig.savefig("catplot.png")
    return ax.fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_heat = df[
        (df["height"].quantile(0.025) <= df["height"])
        & (df["height"].quantile(0.975) >= df["height"])
        & (df["weight"].quantile(0.025) <= df["weight"])
        & (df["weight"].quantile(0.975) >= df["weight"])
    ]
    df_heat = df_heat[(df_heat["ap_lo"] <= df_heat["ap_hi"])]

    # Calculate the correlation matrix
    corr = df_heat.corr()
    # Generate a mask for the upper triangle

    mask = np.zeros_like(corr)
    mask[np.triu_indices_from(mask)] = True
    # Set up the matplotlib figure

    with sns.axes_style("white"):
        fig, ax = plt.subplots(figsize=(11, 9))
        # Draw the heatmap with 'sns.heatmap()
        sns.heatmap(
            corr,
            linewidths=0.5,
            annot=True,
            fmt=".1f",
            mask=mask,
            square=True,
            center=0,
            vmin=-0.08,
            vmax=0.24,
            cbar_kws={"shrink": 0.45, "format": "%.2f"},
        )

        # Do not modify the next two lines
        fig.savefig("heatmap.png")
        return fig

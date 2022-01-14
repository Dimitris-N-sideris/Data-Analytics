import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")
    # Create scatter plot
    plt.scatter(y=df["CSIRO Adjusted Sea Level"], x=df["Year"])
    earliest_year = df["Year"].min()
    year_range = pd.DataFrame({"Year": range(earliest_year, 2051)})
    # Create first line of best fit
    res = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    plt.plot(
        year_range["Year"],
        res.intercept + res.slope * year_range["Year"],
        "r",
        label="fitted line",
    )
    # Create second line of best fit
    df_latest = df[df["Year"] >= 2000]
    year_range = year_range[year_range["Year"] >= 2000]
    res2 = linregress(df_latest["Year"], df_latest["CSIRO Adjusted Sea Level"])
    plt.plot(
        year_range["Year"],
        res2.intercept + res2.slope * year_range["Year"],
        "r",
        label="fitted2",
    )

    # Add labels and title
    plt.title("Rise in Sea Level")
    plt.ylabel("Sea Level (inches)")
    plt.xlabel("Year")

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig("sea_level_plot.png")
    return plt.gca()

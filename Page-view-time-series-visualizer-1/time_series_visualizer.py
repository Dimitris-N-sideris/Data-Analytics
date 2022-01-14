import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters

register_matplotlib_converters()


# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv")
df.set_index("date", inplace=True)
# Clean data
df = df[
    (df["value"].quantile(0.975) >= df["value"])
    & (df["value"].quantile(0.025) <= df["value"])
]


def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize=(8, 4))

    df.plot(
        xlabel="Date",
        ylabel="Page Views",
        ax=ax,
        title="Daily freeCodeCamp Forum Page Views 5/2016-12/2019",
        colormap="autumn",
    )
    # Save image and return fig (don't change this part)
    fig.savefig("line_plot.png")
    return fig


def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar = df_bar.reset_index()
    df_bar["date"] = pd.to_datetime(df_bar["date"])
    # df_bar['day'] = df_bar['date'].dt.day
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ]
    df_bar["months"] = pd.Categorical(
        df_bar.date.dt.strftime("%B"), categories=months, ordered=True
    )
    df_bar["year"] = df_bar["date"].dt.year

    # df_bar =  df_bar.groupby(['year', 'month']).mean()
    # print(df_bar.pivot(columns= ['year','month','value']))
    df_bar = pd.pivot_table(
        data=df_bar, index=df_bar["year"], columns="months", values="value"
    )
    # Draw bar plot
    fig, ax = plt.subplots(figsize=(8, 4))

    df_bar.plot(xlabel="Years", ylabel="Average Page Views", kind="bar", rot=0, ax=ax)
    ax.legend(bbox_to_anchor=(1, 1.02), loc="upper left")
    # Save image and return fig (don't change this part)
    fig.savefig("bar_plot.png")
    return fig


def draw_box_plot():
    # Prepare data for box plots (this part is done!)

    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box["date"] = pd.to_datetime(df_box["date"])
    df_box["year"] = [d.year for d in df_box.date]
    df_box["month"] = [d.strftime("%b") for d in df_box.date]
    months = [
        "Jan",
        "Feb",
        "Mar",
        "Apr",
        "May",
        "Jun",
        "Jul",
        "Aug",
        "Sep",
        "Oct",
        "Nov",
        "Dec",
    ]
    df_box["month"] = pd.Categorical(df_box["month"], categories=months, ordered=True)
    # Draw box plots (using Seaborn)
    fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(30, 15))

    sns.boxplot(x="year", y="value", data=df_box, palette="Set3", ax=ax1)
    ax1.set_xlabel("Year")
    ax1.set_ylabel("Page Views")
    ax1.set_title("Year-wise Box Plot (Trend)")

    sns.boxplot(x="month", y="value", data=df_box, palette="Set3", ax=ax2)
    ax2.set_xlabel("Month")
    ax2.set_ylabel("Page Views")
    ax2.set_title("Month-wise Box Plot (Seasonality)")

    # Save image and return fig (don't change this part)
    fig.savefig("box_plot.png")
    return fig

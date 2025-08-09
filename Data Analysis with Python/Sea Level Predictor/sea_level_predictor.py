import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read the CSV data into a Pandas DataFrame
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    plt.scatter(df["Year"], df["CSIRO Adjusted Sea Level"], label="Data", alpha=0.6)

    # First line of best fit (1880 → latest year)
    slope1, intercept1, r_value1, p_value1, std_err1 = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    years_extended1 = range(1880, 2051)
    plt.plot(years_extended1, slope1 * pd.Series(years_extended1) + intercept1, 'r', label="Best fit: All data")

    # Second line of best fit (2000 → latest year)
    df_recent = df[df["Year"] >= 2000]
    slope2, intercept2, r_value2, p_value2, std_err2 = linregress(df_recent["Year"], df_recent["CSIRO Adjusted Sea Level"])
    years_extended2 = range(2000, 2051)
    plt.plot(years_extended2, slope2 * pd.Series(years_extended2) + intercept2, 'g', label="Best fit: 2000+ data")

    # Labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    plt.legend()

    # Save and return the plot
    plt.savefig('sea_level_plot.png')
    return plt.gca()

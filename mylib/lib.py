"""
library file
"""

import pandas as pd
import matplotlib.pyplot as plt


# Data Loading
def load_dataset(dataset):
    # load data
    df = pd.read_csv(dataset)
    return df


# Data Operations
def return_mean(df, col):
    # return mean
    mean = df[col].mean()
    return mean


def return_median(df, col):
    # return median
    median = df[col].median()
    return median


def return_std(df, col):
    # return std
    std = df[col].std()
    return std


def return_quantile(df, col, num):
    # return quantile
    quantile = df[col].quantile(num)
    return quantile


# Data Vizualization
def generate_histogram(df, render):
    """Generate and save a histogram for the urbanization index."""
    df["urbanindex"] = pd.to_numeric(df["urbanindex"], errors="coerce")
    plt.figure(figsize=(12, 6))
    plt.hist(df["urbanindex"].dropna(), bins=20, edgecolor="black")
    plt.title("Distribution of Urbanization Index Across Districts")
    plt.xlabel("Urbanization Index")
    plt.ylabel("Frequency")
    if not render:
        plt.savefig("urbanization_index_distribution.png")
    else:
        plt.show()
    plt.close()


def generate_line(df, render):
    """Generate and save a line plot for urbanization index groupings."""
    df["urbanindex"] = pd.to_numeric(df["urbanindex"], errors="coerce")
    group_counts = df.groupby(["grouping"]).size().sort_index()
    plt.figure(figsize=(12, 8))
    group_counts.plot(kind="line", colormap="Set1")
    plt.title("Urbanization Groupings Across Congressional Districts")
    plt.xlabel("Urbanization Group")
    plt.ylabel("Count")
    if not render:
        plt.savefig("urbanization_groups.png")
    else:
        plt.show()
    plt.close()


def generate_bar(df, render):
    """Generate and save a bar plot for the dataset"""
    avg_district_type = df[["rural", "exurban", "suburban", "urban"]].mean()
    plt.figure(figsize=(15, 6))
    avg_district_type.plot(kind="bar", color="salmon")
    plt.title("Average Population Distribution")
    plt.xlabel("District Type")
    plt.ylabel("Percentage of Population")
    if not render:
        plt.savefig("district_population_distribution.png")
    else:
        plt.show()
    plt.close()

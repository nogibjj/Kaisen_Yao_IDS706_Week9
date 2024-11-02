"""
Main CLI or app entry point
"""

from mylib.lib import (
    load_dataset,
    return_mean,
    return_quantile,
    return_median,
    return_std,
    generate_histogram,
    generate_line,
    generate_bar,
)


def general_describe(dataset):
    """General describe of the dataset."""
    df = load_dataset(dataset)
    return df.describe()


def custom_describe(dataset, col):
    """Custom describe for a specific column."""
    df = load_dataset(dataset)
    describe_dict = {
        "name": col,
        "mean": return_mean(df, col),
        "std": return_std(df, col),
        "median": return_median(df, col),
        "25 quantile": return_quantile(df, col, 0.25),
    }
    return describe_dict


def general_viz_combined(df, render):
    """Generates and saves all the figures at once."""
    generate_histogram(df, render)
    generate_line(df, render)
    generate_bar(df, render)


def save_to_markdown(dataset):
    """Save a summary report to a markdown file."""
    df = load_dataset(dataset)
    describe = general_describe(dataset)
    markdown_table1 = describe.to_markdown()
    general_viz_combined(df, False)
    # Write the markdown table to a file
    with open("summary.md", "w", encoding="utf-8") as file:
        file.write("Describe:\n")
        file.write(markdown_table1)
        file.write("\n\n")  # Add a new line
        file.write("![Urbanization_viz1](urbanization_index_distribution.png)\n")
        file.write("\n\n")  # Add a new line
        file.write("![Urbanization_viz2](urbanization_groups.png)\n")
        file.write("\n\n")  # Add a new line
        file.write("![Urbanization_viz3](district_population_distribution.png)\n")

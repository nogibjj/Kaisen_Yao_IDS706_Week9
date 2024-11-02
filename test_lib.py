"""
Test goes here
"""

from mylib.lib import (
    load_dataset,
    return_mean,
    return_quantile,
    return_median,
    return_std,
)

dataset = "https://raw.githubusercontent.com/fivethirtyeight/data/master/district-urbanization-index-2022/urbanization-index-2022.csv"


def test_load_dataset():
    """test that loading the csv will work"""
    df = load_dataset(dataset)
    assert df is not None
    assert df.shape == (435, 10)


def test_stats():
    """test that checks the data operations is working"""
    df = load_dataset(dataset)
    mean_test = return_mean(df, "pvi_22")
    quantile_test = return_quantile(df, "pvi_22", 0.25)
    median_test = return_median(df, "pvi_22")
    std_test = return_std(df, "pvi_22")
    describe_test = df.describe()
    assert describe_test.loc["mean", "pvi_22"] == mean_test
    assert describe_test.loc["std", "pvi_22"] == std_test
    assert describe_test.loc["25%", "pvi_22"] == quantile_test
    assert median_test == -2.27852


if __name__ == "__main__":
    test_load_dataset()
    test_stats()

"""
Test goes here
"""

from main import general_describe, custom_describe, save_to_markdown

dataset = "https://raw.githubusercontent.com/fivethirtyeight/data/master/district-urbanization-index-2022/urbanization-index-2022.csv"


def test_describe():
    """test describe is actually working"""
    describe_test = general_describe(dataset)
    assert describe_test.shape == (8, 7)


def test_two_describes():
    """test .describe with custom describe function"""
    describe_test = general_describe(dataset)
    custom_test = custom_describe(dataset, "pvi_22")
    assert describe_test.loc["mean", "pvi_22"] == custom_test["mean"]
    assert describe_test.loc["std", "pvi_22"] == custom_test["std"]
    assert describe_test.loc["25%", "pvi_22"] == custom_test["25 quantile"]


def test_summary_and_viz_to_markdown():
    """converts to markdown()"""
    save_to_markdown(dataset)


if __name__ == "__main__":
    test_describe()
    test_two_describes()
    test_summary_and_viz_to_markdown()

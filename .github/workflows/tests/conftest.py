import pandas as pd
from splink.datasets import splink_datasets

pd.options.display.max_rows = 1000


import pytest


@pytest.fixture
def historical_50k_df():
    return splink_datasets.historical_50k

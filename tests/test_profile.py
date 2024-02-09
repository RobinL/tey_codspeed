import pytest
from splink.duckdb.linker import DuckDBLinker


@pytest.mark.benchmark
def test_profile(historical_50k_df):

    settings = {
        "link_type": "dedupe_only",
    }
    linker = DuckDBLinker(historical_50k_df, settings)

    linker.profile_columns(
        ["first_name", "postcode_fake", "substr(dob, 1,4)"], top_n=10, bottom_n=5
    )

    1 + 1

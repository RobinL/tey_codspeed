from splink.duckdb.linker import DuckDBLinker


def test_profile(historical_50k_df):
    # Your test code here

    # Simple settings dictionary will be used for exploratory analysis
    settings = {
        "link_type": "dedupe_only",
    }
    linker = DuckDBLinker(historical_50k_df, settings)

    linker.profile_columns(
        ["first_name", "postcode_fake", "substr(dob, 1,4)"], top_n=10, bottom_n=5
    )

import duckdb


def test_duckdb_works():
    assert duckdb.sql("SELECT 1 + 1").fetchone()[0] == 2

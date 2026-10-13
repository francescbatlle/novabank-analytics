from customers import COUNTRY_WEIGHTS, SIMULATION_END, SIMULATION_START, generate_customers


def test_number_of_rows():
    """The table has one row per requested customer."""
    df = generate_customers(1000, seed=42)
    assert len(df) == 1000


def test_customer_ids_are_unique():
    """No customer_id appears more than once."""
    df = generate_customers(1000, seed=42)
    assert df["customer_id"].is_unique


def test_only_valid_countries():
    """Every country is one of the countries in COUNTRY_WEIGHTS."""
    df = generate_customers(1000, seed=42)
    valid_countries = list(COUNTRY_WEIGHTS.keys())
    assert df["country"].isin(valid_countries).all()


def test_signup_dates_within_simulation_period():
    """Every signup date falls inside the simulation period."""
    df = generate_customers(1000, seed=42)
    assert df["signup_date"].between(SIMULATION_START, SIMULATION_END).all()


def test_same_seed_gives_same_customers():
    """The same seed always produces exactly the same table."""
    df1 = generate_customers(1000, seed=42)
    df2 = generate_customers(1000, seed=42)
    assert df1.equals(df2)


def test_different_seed_gives_different_customers():
    """A different seed produces a different table, so the seed is really used."""
    df1 = generate_customers(1000, seed=42)
    df2 = generate_customers(1000, seed=7)
    assert not df1.equals(df2)
import numpy as np
import pandas as pd

# Customer share by country, based on Revolut's publicly reported
# retail customers per market (late 2025 / early 2026).
# FR 7.0M, ES 6.3M, IT ~4.5M (interpolated), DE 3.0M, NL 1.5M.
COUNTRY_WEIGHTS = {
    "ES": 0.28,
    "DE": 0.14,
    "FR": 0.31,
    "NL": 0.07,
    "IT": 0.20,
}

# Acquisition channel shares. Revolut 2025: 63% of new retail customers
# came via organic channels and referrals (sourced). The split within
# each group (organic vs referral, paid_social vs partnership) is an assumption.
CHANNEL_WEIGHTS = {
    "organic": 0.38,
    "referral": 0.25,
    "paid_social": 0.30,
    "partnership": 0.07,
}

# Plan shares. Total paid share (~8%) estimated from Revolut 2025 subscription
# revenue (GBP 708M) and 68.3M retail customers. Revolut does not publish the
# split by plan, so the distribution across paid tiers is an assumption
# (more customers on cheaper plans).
PLAN_WEIGHTS = {
    "standard": 0.920,
    "plus": 0.035,
    "premium": 0.025,
    "metal": 0.015,
    "ultra": 0.005,
}

def generate_customers(n_customers: int, seed: int) -> pd.DataFrame:
    rng = np.random.default_rng(seed)

    # Country
    countries = list(COUNTRY_WEIGHTS.keys())
    country_probabilities = list(COUNTRY_WEIGHTS.values())
    country = rng.choice(countries, size=n_customers, p=country_probabilities)

    # Acquisition channel
    channels = list(CHANNEL_WEIGHTS.keys())
    channel_probabilities = list(CHANNEL_WEIGHTS.values())
    acquisition_channel = rng.choice(channels, size=n_customers, p=channel_probabilities)

    # Plan
    plans = list(PLAN_WEIGHTS.keys())
    plan_probabilities = list(PLAN_WEIGHTS.values())
    plan = rng.choice(plans, size=n_customers, p=plan_probabilities)

    # Customer ID
    customer_id = []
    for i in range(1, n_customers + 1):
        number = str(i).zfill(6)  # Pad to 6 digits so IDs sort correctly as text
        customer_id.append("C" + number)

    return pd.DataFrame({
        'customer_id': customer_id,
        'country': country,
        'acquisition_channel': acquisition_channel,
        'plan': plan,
    })

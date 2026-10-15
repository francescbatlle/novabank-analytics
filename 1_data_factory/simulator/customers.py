import numpy as np
import pandas as pd

"""Generate NovaBank's customers table.

Design decisions:
- All customers sign up within the simulation period (2025), as if NovaBank
  launched in January. Simplification: no pre-existing customer base.
- Signups grow MONTHLY_GROWTH per month, calibrated on Revolut 2025 data.
- Churn is not a column here: a real bank does not know at signup who will
  leave. It will be simulated through transaction activity instead.
- Country, channel and plan are independent of signup date, so sorting the
  dates alone does not bias the other columns.
"""

# Name for the customers table.
CustomersTable = pd.DataFrame

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

# Monthly growth in new signups. Calibrated on Revolut 2025: 16M new customers
# in the year (~1.33M/month on average) vs ~1.76M/month at year end
# ("1M new customers every 17 days"). December ~32% above the average month
# implies ~5-6% monthly growth. We use 5% (conservative end).
MONTHLY_GROWTH = 0.05

# Simulation period: NovaBank's first full year. Shared by all generators.
SIMULATION_START = "2025-01-01"
SIMULATION_END = "2025-12-31"


def generate_customers(n_customers: int, seed: int = 42) -> CustomersTable:
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

    # Signup date: later days are more likely, growing MONTHLY_GROWTH per month
    start = pd.Timestamp(SIMULATION_START)
    days = np.arange(365)
    day_weights = (1 + MONTHLY_GROWTH) ** (days / 30.4)  # ~30.4 days per month
    day_probabilities = day_weights / day_weights.sum()
    days_after_start = rng.choice(days, size=n_customers, p=day_probabilities)
    signup_date = start + pd.to_timedelta(days_after_start, unit="D")
    signup_date = signup_date.sort_values()  # Earlier customers get lower IDs

    # Customer ID
    customer_id = []
    for i in range(1, n_customers + 1):
        number = str(i).zfill(6)  # Pad to 6 digits so IDs sort correctly as text
        customer_id.append("C" + number)

    return CustomersTable({
        "customer_id": customer_id,
        "signup_date": signup_date,
        "country": country,
        "acquisition_channel": acquisition_channel,
        "plan": plan,
    })

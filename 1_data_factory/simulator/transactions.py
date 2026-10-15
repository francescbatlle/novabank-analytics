import numpy as np
import pandas as pd

from customers import SIMULATION_END, CustomersTable

# Name for the transactions table. Same as pd.DataFrame, but easier to read.
TransactionsTable = pd.DataFrame


#Average payments per customer per active day. Chosen so the simulation
# produces ~2M transactions (50,000 customers x ~165 active days on average).
PAYMENTS_PER_DAY = 0.25

# Payment method shares. Based on ECB SPACE 2024 (euro area): online payments
# are 21% of day-to-day payments and cash is 52% of point-of-sale payments.
# in store ~64%. The in-store split between physical card and mobile wallet
# is an assumption (neobank customers use mobile wallets heavily).
PAYMENT_METHOD_WEIGHTS = {
    "card": 0.36,
    "mobile_wallet": 0.28,
    "online": 0.36,
}

def generate_transactions(customers: CustomersTable, seed: int = 42) -> TransactionsTable:
    rng = np.random.default_rng(seed)
    
    # customer_id: how many payments each customer makes (defines n_transactions)
    end = pd.Timestamp(SIMULATION_END)
    customer_id = []
    for i in range(len(customers)):
        this_customer = customers["customer_id"][i]
        signup = customers["signup_date"][i]
        active_days = (end - signup).days + 1
        n_payments = rng.poisson(active_days * PAYMENTS_PER_DAY)

        for j in range(n_payments):
            customer_id.append(this_customer)

        n_transactions = len(customer_id)
    
    # created_at
    
    # amount_eur
    
    # merchant_category
    
    # payment_method
    payment_methods = list(PAYMENT_METHOD_WEIGHTS.keys())
    payment_probabilities = list(PAYMENT_METHOD_WEIGHTS.values())
    payment_method = rng.choice(payment_methods, size =  n_transactions,  p = payment_probabilities)
    
    # status
    
    # failure_reason
    
    # is_fraud
    
    # transaction_id

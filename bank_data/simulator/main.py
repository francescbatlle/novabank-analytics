import os

from customers import generate_customers

# Configuration
N_CUSTOMERS = 50000
SEED = 42

# 1. Create the folder where the data will be saved
os.makedirs("data/raw", exist_ok=True)

# 2. Generate the customers
customers = generate_customers(N_CUSTOMERS, seed=SEED)

# 3. Save them to a Parquet file
customers.to_parquet("data/raw/customers.parquet", index=False)

# 4. Confirm it worked
print("Saved", len(customers), "customers to data/raw/customers.parquet")

"""
Supplier Performance Analysis

This script evaluates supplier performance using the cleaned supply chain dataset.

The analysis focuses on:
1. Supplier lead time performance
2. Supplier production contribution
3. Supplier shipping cost impact
4. Supplier defect rate impact

The goal is to identify suppliers that may impact supply chain efficiency
and overall supply chain performance.
"""

# -------------------------------------------------
# Import Required Libraries
# -------------------------------------------------

import pandas as pd
import os


# -------------------------------------------------
# Locate Project Directory and Load Dataset
# -------------------------------------------------

# Get the directory where the script is located
script_dir = os.path.dirname(__file__)

# Move one level up to reach the project root folder
project_root = os.path.abspath(os.path.join(script_dir, ".."))

# Define path to cleaned dataset
data_path = os.path.join(project_root, "02_Data", "cleaned_supply_chain_data.csv")

# Load dataset
df = pd.read_csv(data_path)


# -------------------------------------------------
# Supplier Lead Time Analysis
# Calculate average supplier lead time
# -------------------------------------------------

print("\n===== SUPPLIER LEAD TIME ANALYSIS =====")

lead_time = (
    df.groupby("supplier_name")["supplier_lead_time"]
    .mean()
    .sort_values(ascending=False)
)

print(lead_time)


# -------------------------------------------------
# Supplier Production Contribution
# Total production volume provided by each supplier
# -------------------------------------------------

print("\n===== SUPPLIER PRODUCTION CONTRIBUTION =====")

production = (
    df.groupby("supplier_name")["production_volume"]
    .sum()
    .sort_values(ascending=False)
)

print(production)


# -------------------------------------------------
# Supplier Shipping Cost Impact
# Average shipping cost associated with each supplier
# -------------------------------------------------

print("\n===== SUPPLIER SHIPPING COST IMPACT =====")

shipping_cost = (
    df.groupby("supplier_name")["shipping_cost"]
    .mean()
    .sort_values(ascending=False)
)

print(shipping_cost)


# -------------------------------------------------
# Supplier Defect Rate Impact
# Average defect rate associated with each supplier
# -------------------------------------------------

print("\n===== SUPPLIER DEFECT RATE IMPACT =====")

defect_rate = (
    df.groupby("supplier_name")["defect_rate"]
    .mean()
    .sort_values(ascending=False)
)

print(defect_rate)
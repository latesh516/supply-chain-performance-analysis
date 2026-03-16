"""
Data Cleaning Script

Purpose:
Prepare the raw supply chain dataset for analysis.

Steps:
1. Load raw dataset
2. Standardize column names
3. Rename columns for easier analysis
4. Check duplicate SKUs
5. Validate numeric columns
6. Save cleaned dataset
"""

# -------------------------------------------------
# Import Libraries
# -------------------------------------------------

import pandas as pd
from pathlib import Path


# -------------------------------------------------
# Locate Project Root (PORTABLE)
# -------------------------------------------------

script_path = Path(__file__).resolve()

# Move up one folder from script location
project_root = script_path.parents[1]

# Build paths
raw_path = project_root / "02_Data" / "CSV file" / "raw_data.csv"
clean_path = project_root / "02_Data" / "cleaned_supply_chain_data.csv"


# -------------------------------------------------
# Validate Dataset Path
# -------------------------------------------------

print("\nReading dataset from:")
print(raw_path)

if not raw_path.exists():
    raise FileNotFoundError(f"Dataset not found at {raw_path}")


# -------------------------------------------------
# Load Raw Dataset
# -------------------------------------------------

df = pd.read_csv(raw_path)

print("\nOriginal Columns:\n")
print(df.columns)


# -------------------------------------------------
# Standardize Column Names
# -------------------------------------------------

df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
)

print("\nStandardized Columns:\n")
print(df.columns)


# -------------------------------------------------
# Rename Important Columns
# -------------------------------------------------

df = df.rename(columns={
    "number_of_products_sold": "products_sold",
    "revenue_generated": "revenue",
    "stock_levels": "stock_level",
    "shipping_times": "shipping_time",
    "shipping_costs": "shipping_cost",
    "transportation_modes": "transport_mode",
    "production_volumes": "production_volume",
    "manufacturing_costs": "manufacturing_cost",
    "manufacturing_lead_time": "manufacturing_lead_time_days",
    "defect_rates": "defect_rate",
    "lead_times": "supplier_lead_time"
})

print("\nRenamed Columns:\n")
print(df.columns)


# -------------------------------------------------
# Check Duplicate SKUs
# -------------------------------------------------

if "sku" in df.columns:
    duplicate_skus = df["sku"].duplicated().sum()
    print("\nDuplicate SKUs:", duplicate_skus)
else:
    print("\nSKU column not found.")


# -------------------------------------------------
# Validate Numeric Columns
# -------------------------------------------------

numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns

for col in numeric_cols:
    if (df[col] < 0).any():
        print(f"Warning: Negative values found in {col}")


# -------------------------------------------------
# Save Cleaned Dataset
# -------------------------------------------------

df.to_csv(clean_path, index=False)

print("\nClean dataset saved to:")
print(clean_path)

print("\nData cleaning completed successfully.")
"""
Manufacturing Efficiency Analysis

This script evaluates manufacturing performance using the cleaned
supply chain dataset.

The analysis focuses on:
1. Production volume by product category
2. Manufacturing lead time comparison
3. Defect rate analysis
4. Inspection result distribution
5. Manufacturing cost comparison

The objective is to identify potential manufacturing inefficiencies,
quality control issues, and cost drivers across product categories.
"""

# -------------------------------------------------
# Import Required Libraries
# -------------------------------------------------

import pandas as pd
import os


# -------------------------------------------------
# Locate Project Directory and Load Dataset
# -------------------------------------------------

# Identify the current script location
script_dir = os.path.dirname(__file__)

# Navigate to the project root
project_root = os.path.abspath(os.path.join(script_dir, ".."))

# Define path to cleaned dataset
data_path = os.path.join(project_root, "02_Data", "cleaned_supply_chain_data.csv")

# Load dataset
df = pd.read_csv(data_path)


# -------------------------------------------------
# 1. Production Volume by Product Type
# Compare manufacturing output across product categories
# -------------------------------------------------

print("\n===== PRODUCTION VOLUME BY PRODUCT TYPE =====")

production = (
    df.groupby("product_type")["production_volume"]
    .sum()
    .sort_values(ascending=False)
)

print(production)


# -------------------------------------------------
# 2. Manufacturing Lead Time by Product Type
# Measure average production time required for each category
# -------------------------------------------------

print("\n===== MANUFACTURING LEAD TIME BY PRODUCT TYPE =====")

lead_time = (
    df.groupby("product_type")["manufacturing_lead_time_days"]
    .mean()
    .sort_values(ascending=False)
)

print(lead_time)


# -------------------------------------------------
# 3. Defect Rate by Product Type
# Evaluate manufacturing quality performance
# -------------------------------------------------

print("\n===== DEFECT RATE BY PRODUCT TYPE =====")

defect_rate = (
    df.groupby("product_type")["defect_rate"]
    .mean()
    .sort_values(ascending=False)
)

print(defect_rate)


# -------------------------------------------------
# 4. Inspection Result Distribution
# Analyze manufacturing inspection outcomes
# -------------------------------------------------

print("\n===== INSPECTION RESULT DISTRIBUTION =====")

inspection = df["inspection_result"].value_counts()

print(inspection)


# -------------------------------------------------
# 5. Average Manufacturing Cost by Product Type
# Compare production cost efficiency across categories
# -------------------------------------------------

print("\n===== AVERAGE MANUFACTURING COST BY PRODUCT TYPE =====")

manufacturing_cost = (
    df.groupby("product_type")["manufacturing_cost"]
    .mean()
    .sort_values(ascending=False)
)

print(manufacturing_cost)
"""
Logistics Cost and Transportation Analysis

This script analyzes logistics performance using the cleaned supply chain dataset.

The analysis focuses on:
1. Shipping cost comparison across carriers
2. Shipping time performance by carrier
3. Transportation cost by transport mode
4. Cost comparison across shipping routes

The objective is to identify logistics cost drivers and evaluate
transportation efficiency within the supply chain network.
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

# Navigate to the project root folder
project_root = os.path.abspath(os.path.join(script_dir, ".."))

# Define path to cleaned dataset
data_path = os.path.join(project_root, "02_Data", "cleaned_supply_chain_data.csv")

# Load dataset
df = pd.read_csv(data_path)


# -------------------------------------------------
# 1. Shipping Cost by Carrier
# Evaluate average shipping cost across different carriers
# -------------------------------------------------

print("\n===== SHIPPING COST BY CARRIER =====")

carrier_cost = (
    df.groupby("shipping_carrier")["shipping_cost"]
    .mean()
    .sort_values(ascending=False)
)

print(carrier_cost)


# -------------------------------------------------
# 2. Shipping Time by Carrier
# Compare delivery performance between carriers
# -------------------------------------------------

print("\n===== SHIPPING TIME BY CARRIER =====")

carrier_time = (
    df.groupby("shipping_carrier")["shipping_time"]
    .mean()
    .sort_values(ascending=False)
)

print(carrier_time)


# -------------------------------------------------
# 3. Transport Cost by Mode
# Analyze cost differences between transportation modes
# -------------------------------------------------

print("\n===== TRANSPORT COST BY MODE =====")

mode_cost = (
    df.groupby("transportation_mode")["transport_cost"]
    .mean()
    .sort_values(ascending=False)
)

print(mode_cost)


# -------------------------------------------------
# 4. Route Cost Analysis
# Identify routes with the highest logistics costs
# -------------------------------------------------

print("\n===== TRANSPORT COST BY ROUTE =====")

route_cost = (
    df.groupby("route")["transport_cost"]
    .mean()
    .sort_values(ascending=False)
)

print(route_cost)
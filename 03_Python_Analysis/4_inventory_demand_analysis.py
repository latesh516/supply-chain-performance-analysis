"""
Inventory and Demand Analysis

This script analyzes the relationship between product demand and
inventory availability within the supply chain dataset.

The analysis focuses on:
1. Inventory turnover by SKU
2. Identification of stockout-risk products
3. Demand vs stock gap analysis
4. Detection of excess inventory
5. Average stock levels by product category

The goal is to identify potential inventory planning issues such as
stockouts, excess stock, and mismatches between demand and inventory levels.
"""

# -------------------------------------------------
# Import Required Libraries
# -------------------------------------------------

import pandas as pd
import os


# -------------------------------------------------
# Locate Project Directory and Load Dataset
# -------------------------------------------------

# Identify current script location
script_dir = os.path.dirname(__file__)

# Navigate to project root
project_root = os.path.abspath(os.path.join(script_dir, ".."))

# Define path to cleaned dataset
data_path = os.path.join(project_root, "02_Data", "cleaned_supply_chain_data.csv")

# Load dataset
df = pd.read_csv(data_path)


# -------------------------------------------------
# 1. Inventory Turnover by SKU
# Measures how quickly inventory is sold relative to stock level
# -------------------------------------------------

print("\n===== INVENTORY TURNOVER =====")

df["inventory_turnover"] = df["products_sold"] / df["stock_level"].replace(0, 1)

inventory_turnover = (
    df[["sku", "inventory_turnover"]]
    .sort_values(by="inventory_turnover", ascending=False)
)

print(inventory_turnover.head(10))


# -------------------------------------------------
# 2. Stockout Risk Identification
# Products with low stock but high demand
# -------------------------------------------------

print("\n===== STOCKOUT RISK PRODUCTS =====")

stockout_risk = df[
    (df["stock_level"] < 10) &
    (df["products_sold"] > df["products_sold"].mean())
]

print(stockout_risk[["sku", "product_type", "stock_level", "products_sold"]])


# -------------------------------------------------
# 3. Demand vs Stock Gap Analysis
# Measures difference between demand and available inventory
# -------------------------------------------------

print("\n===== DEMAND VS STOCK GAP =====")

df["demand_stock_gap"] = df["products_sold"] - df["stock_level"]

gap = df[["sku", "demand_stock_gap"]].sort_values(
    by="demand_stock_gap",
    ascending=False
)

print(gap.head(10))


# -------------------------------------------------
# 4. Excess Inventory Detection
# Identify products with high stock but relatively low demand
# -------------------------------------------------

print("\n===== EXCESS INVENTORY CHECK =====")

excess_inventory = df[
    (df["stock_level"] > df["stock_level"].mean()) &
    (df["products_sold"] < df["products_sold"].mean())
]

print(excess_inventory[["sku", "product_type", "stock_level", "products_sold"]])


# -------------------------------------------------
# 5. Average Stock Level by Product Type
# Compare inventory levels across product categories
# -------------------------------------------------

print("\n===== AVERAGE STOCK BY PRODUCT TYPE =====")

avg_stock = (
    df.groupby("product_type")["stock_level"]
    .mean()
    .sort_values(ascending=False)
)

print(avg_stock)
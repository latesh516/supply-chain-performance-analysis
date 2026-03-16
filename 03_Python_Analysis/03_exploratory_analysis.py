"""
Exploratory Data Analysis (EDA)

This script performs exploratory analysis on the cleaned supply chain dataset.

The goal of this analysis is to understand key patterns in:
1. Product demand and revenue performance
2. Top selling SKUs
3. Customer demographic distribution
4. Inventory availability vs product demand
5. Supplier lead time performance
6. Manufacturing defect rates
7. Transportation cost by mode
8. Route cost comparison

These insights help identify potential inefficiencies in demand planning,
inventory management, supplier performance, manufacturing quality,
and logistics operations.
"""

# -------------------------------------------------
# Import Required Libraries
# -------------------------------------------------

import pandas as pd
import os


# -------------------------------------------------
# Locate Project Directory and Load Dataset
# -------------------------------------------------

# Identify current script directory
script_dir = os.path.dirname(__file__)

# Navigate to project root
project_root = os.path.abspath(os.path.join(script_dir, ".."))

# Define path to cleaned dataset
data_path = os.path.join(project_root, "02_Data", "cleaned_supply_chain_data.csv")

# Load dataset
df = pd.read_csv(data_path)


# -------------------------------------------------
# Dataset Overview
# -------------------------------------------------

print("\n===== DATASET OVERVIEW =====")
print(df.head())


# -------------------------------------------------
# 1. Revenue by Product Type
# Identify which product categories generate the highest revenue
# -------------------------------------------------

print("\n===== REVENUE BY PRODUCT TYPE =====")

print(
    df.groupby("product_type")["revenue"]
    .sum()
    .sort_values(ascending=False)
)


# -------------------------------------------------
# 2. Top Selling SKUs
# Identify the products with the highest sales volume
# -------------------------------------------------

print("\n===== TOP SELLING SKUS =====")

print(
    df.groupby("sku")["products_sold"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)


# -------------------------------------------------
# 3. Sales by Customer Demographics
# Understand how sales are distributed across customer segments
# -------------------------------------------------

print("\n===== SALES BY CUSTOMER DEMOGRAPHICS =====")

print(
    df.groupby("customer_demographics")["products_sold"]
    .sum()
)


# -------------------------------------------------
# 4. Stock vs Demand
# Compare product demand with current inventory levels
# -------------------------------------------------

print("\n===== STOCK VS SALES =====")

print(
    df[["sku", "stock_level", "products_sold"]]
    .sort_values(by="products_sold", ascending=False)
    .head(10)
)


# -------------------------------------------------
# 5. Supplier Lead Time Analysis
# Evaluate supplier performance based on delivery lead time
# -------------------------------------------------

print("\n===== SUPPLIER LEAD TIME =====")

print(
    df.groupby("supplier_name")["supplier_lead_time"]
    .mean()
    .sort_values(ascending=False)
)


# -------------------------------------------------
# 6. Defect Rate by Product Type
# Analyze manufacturing quality issues across product categories
# -------------------------------------------------

print("\n===== DEFECT RATE BY PRODUCT =====")

print(
    df.groupby("product_type")["defect_rate"]
    .mean()
    .sort_values(ascending=False)
)


# -------------------------------------------------
# 7. Transport Cost by Mode
# Compare logistics cost across transportation methods
# -------------------------------------------------

print("\n===== TRANSPORT COST BY MODE =====")

print(
    df.groupby("transportation_mode")["transport_cost"]
    .mean()
    .sort_values(ascending=False)
)


# -------------------------------------------------
# 8. Route Cost Analysis
# Identify which logistics routes are the most expensive
# -------------------------------------------------

print("\n===== ROUTE COST ANALYSIS =====")

print(
    df.groupby("route")["transport_cost"]
    .mean()
    .sort_values(ascending=False)
)
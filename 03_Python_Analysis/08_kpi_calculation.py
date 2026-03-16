"""
Supply Chain KPI Calculation

This script calculates key performance indicators (KPIs) used to evaluate
overall supply chain performance.

The KPIs are grouped into five operational areas:

1. Demand KPIs
   - Total revenue
   - Total units sold
   - Top revenue generating product category

2. Inventory KPIs
   - Average stock level
   - Inventory turnover

3. Supplier KPIs
   - Average supplier lead time
   - Top supplier based on production volume

4. Manufacturing KPIs
   - Average defect rate
   - Average manufacturing cost
   - Average manufacturing lead time

5. Logistics KPIs
   - Average shipping cost
   - Average shipping time
   - Average transportation cost

These KPIs provide a high-level overview of supply chain efficiency and
help identify potential improvement areas across demand planning,
inventory management, supplier performance, manufacturing efficiency,
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

# Identify current script location
script_dir = os.path.dirname(__file__)

# Navigate to project root folder
project_root = os.path.abspath(os.path.join(script_dir, ".."))

# Define path to cleaned dataset
data_path = os.path.join(project_root, "02_Data", "cleaned_supply_chain_data.csv")

# Load dataset
df = pd.read_csv(data_path)


# -------------------------------------------------
# 1. Demand KPIs
# -------------------------------------------------

print("\n===== DEMAND KPIs =====")

total_revenue = df["revenue"].sum()
total_units = df["products_sold"].sum()

print("Total Revenue:", round(total_revenue, 2))
print("Total Units Sold:", total_units)

top_product = df.groupby("product_type")["revenue"].sum().idxmax()
print("Top Revenue Product Type:", top_product)


# -------------------------------------------------
# 2. Inventory KPIs
# -------------------------------------------------

print("\n===== INVENTORY KPIs =====")

avg_stock = df["stock_level"].mean()
print("Average Stock Level:", round(avg_stock, 2))

inventory_turnover = df["products_sold"].sum() / df["stock_level"].mean()
print("Inventory Turnover:", round(inventory_turnover, 2))


# -------------------------------------------------
# 3. Supplier KPIs
# -------------------------------------------------

print("\n===== SUPPLIER KPIs =====")

avg_supplier_lead = df["supplier_lead_time"].mean()
print("Average Supplier Lead Time:", round(avg_supplier_lead, 2))

top_supplier = df.groupby("supplier_name")["production_volume"].sum().idxmax()
print("Top Supplier by Production:", top_supplier)


# -------------------------------------------------
# 4. Manufacturing KPIs
# -------------------------------------------------

print("\n===== MANUFACTURING KPIs =====")

avg_defect = df["defect_rate"].mean()
print("Average Defect Rate:", round(avg_defect, 2))

avg_mfg_cost = df["manufacturing_cost"].mean()
print("Average Manufacturing Cost:", round(avg_mfg_cost, 2))

avg_mfg_lead = df["manufacturing_lead_time_days"].mean()
print("Average Manufacturing Lead Time:", round(avg_mfg_lead, 2))


# -------------------------------------------------
# 5. Logistics KPIs
# -------------------------------------------------

print("\n===== LOGISTICS KPIs =====")

avg_shipping_cost = df["shipping_cost"].mean()
print("Average Shipping Cost:", round(avg_shipping_cost, 2))

avg_shipping_time = df["shipping_time"].mean()
print("Average Shipping Time:", round(avg_shipping_time, 2))

avg_transport_cost = df["transport_cost"].mean()
print("Average Transport Cost:", round(avg_transport_cost, 2))
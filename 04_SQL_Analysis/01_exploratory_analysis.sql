/* SUPPLY CHAIN PERFORMANCE ANALYSIS */

CREATE DATABASE Supply_Chain_Analysis;
GO
USE Supply_Chain_Analysis;
GO

/* =========================================================*/
/* 1. Create Table */

CREATE TABLE supply_chain (
product_type VARCHAR(50),
sku VARCHAR(20),
price DECIMAL(10,2),
availability INT,
products_sold INT,
revenue DECIMAL(12,2),
customer_demographics VARCHAR(20),
stock_level INT,
supplier_lead_time INT,
order_quantity INT,
shipping_time INT,
shipping_carrier VARCHAR(50),
shipping_cost DECIMAL(10,2),
supplier_name VARCHAR(50),
location VARCHAR(50),
total_supply_chain_lead_time INT,
production_volume INT,
manufacturing_lead_time_days INT,
manufacturing_cost DECIMAL(10,2),
inspection_result VARCHAR(20),
defect_rate DECIMAL(5,2),
transportation_mode VARCHAR(20),
route VARCHAR(20),
transport_cost DECIMAL(10,2)
);

/* =========================================================*/
/* 2. Load Data */

BULK INSERT supply_chain
FROM 'C:\1. supply chain project\02_Data\cleaned_supply_chain_data.csv'
WITH (
FORMAT='CSV',
FIRSTROW=2,
FIELDTERMINATOR=',',
ROWTERMINATOR='\n',
TABLOCK
);

/* =========================================================*/
/* 3. Data Validation */

SELECT COUNT(*) AS total_records FROM supply_chain;
SELECT * FROM supply_chain;

/* =========================================================*/
/* 4. Demand Analysis */

-- Revenue by Product Type
SELECT product_type,SUM(revenue) AS total_revenue
FROM supply_chain
GROUP BY product_type
ORDER BY total_revenue DESC;

-- Top Selling SKUs
SELECT TOP 10 sku,SUM(products_sold) AS total_units_sold
FROM supply_chain
GROUP BY sku
ORDER BY total_units_sold DESC;

-- Sales by Customer Demographics
SELECT customer_demographics,SUM(products_sold) AS total_sales
FROM supply_chain
GROUP BY customer_demographics
ORDER BY total_sales DESC;

/* =========================================================*/
/* 5. Inventory Analysis */

-- Stock vs Demand
SELECT TOP 10 sku,stock_level,products_sold
FROM supply_chain
ORDER BY products_sold DESC;

-- Products at Risk of Stockout
SELECT TOP 10 sku,product_type,stock_level
FROM supply_chain
ORDER BY stock_level ASC;

-- Slow Moving Inventory
SELECT sku,product_type,stock_level,products_sold
FROM supply_chain
WHERE stock_level>200 AND products_sold<50
ORDER BY stock_level DESC;

-- Inventory Turnover
SELECT sku,
SUM(products_sold)*1.0/NULLIF(AVG(stock_level),0) AS inventory_turnover
FROM supply_chain
GROUP BY sku
ORDER BY inventory_turnover DESC;

/* =========================================================*/
/* 6. Supplier Analysis */

-- Supplier Lead Time
SELECT supplier_name,AVG(supplier_lead_time) AS avg_lead_time_days
FROM supply_chain
GROUP BY supplier_name
ORDER BY avg_lead_time_days DESC;

-- Supplier Production Contribution
SELECT supplier_name,SUM(production_volume) AS total_production
FROM supply_chain
GROUP BY supplier_name
ORDER BY total_production DESC;

/* =========================================================*/
/* 7. Manufacturing Analysis */

-- Production Volume by Product
SELECT product_type,SUM(production_volume) AS total_production
FROM supply_chain
GROUP BY product_type
ORDER BY total_production DESC;

-- Defect Rate by Product
SELECT product_type,AVG(defect_rate) AS avg_defect_rate
FROM supply_chain
GROUP BY product_type
ORDER BY avg_defect_rate DESC;

-- Inspection Result Distribution
SELECT inspection_result,COUNT(*) AS total_records
FROM supply_chain
GROUP BY inspection_result;

/* =========================================================*/
/* 8. Logistics Analysis */

-- Shipping Cost by Carrier
SELECT shipping_carrier,AVG(shipping_cost) AS avg_shipping_cost
FROM supply_chain
GROUP BY shipping_carrier
ORDER BY avg_shipping_cost DESC;

-- Shipping Time by Carrier
SELECT shipping_carrier,AVG(shipping_time) AS avg_shipping_time
FROM supply_chain
GROUP BY shipping_carrier
ORDER BY avg_shipping_time DESC;

-- Transport Cost by Mode
SELECT transportation_mode,AVG(transport_cost) AS avg_transport_cost
FROM supply_chain
GROUP BY transportation_mode
ORDER BY avg_transport_cost DESC;

-- Route Cost Analysis
SELECT route,AVG(transport_cost) AS avg_route_cost
FROM supply_chain
GROUP BY route
ORDER BY avg_route_cost DESC;
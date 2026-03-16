/* =========================================================
   SUPPLY CHAIN KPI CALCULATIONS
========================================================= */

/* =========================================================
   1. DEMAND KPIs
========================================================= */

-- 1.1 Total Revenue
SELECT
    SUM(revenue) AS total_revenue
FROM supply_chain;

-- 1.2 Total Units Sold
SELECT
    SUM(products_sold) AS total_units_sold
FROM supply_chain;

-- 1.3 Revenue by Product Type
SELECT
    product_type,
    SUM(revenue) AS total_revenue
FROM supply_chain
GROUP BY product_type
ORDER BY total_revenue DESC;


/* =========================================================
   2. INVENTORY KPIs
========================================================= */

-- 2.1 Average Stock Level
SELECT
    AVG(stock_level) AS avg_stock_level
FROM supply_chain;

-- 2.2 Inventory Turnover
SELECT
SUM(products_sold) * 1.0 /
(SUM(stock_level) * 1.0 / COUNT(stock_level))
AS inventory_turnover
FROM supply_chain;


/* =========================================================
   3. SUPPLIER KPIs
========================================================= */

-- 3.1 Average Supplier Lead Time
SELECT
    AVG(supplier_lead_time) AS avg_supplier_lead_time
FROM supply_chain;

-- 3.2 Production by Supplier
SELECT
    supplier_name,
    SUM(production_volume) AS total_production
FROM supply_chain
GROUP BY supplier_name
ORDER BY total_production DESC;


/* =========================================================
   4. MANUFACTURING KPIs
========================================================= */

-- 4.1 Average Defect Rate
SELECT
    AVG(defect_rate) AS avg_defect_rate
FROM supply_chain;

-- 4.2 Average Manufacturing Cost
SELECT
    AVG(manufacturing_cost) AS avg_manufacturing_cost
FROM supply_chain;

-- 4.3 Average Manufacturing Lead Time
SELECT
    AVG(manufacturing_lead_time_days) AS avg_mfg_lead_time
FROM supply_chain;


/* =========================================================
   5. LOGISTICS KPIs
========================================================= */

-- 5.1 Average Shipping Cost
SELECT
    AVG(shipping_cost) AS avg_shipping_cost
FROM supply_chain;

-- 5.2 Average Shipping Time
SELECT
    AVG(shipping_time) AS avg_shipping_time
FROM supply_chain;

-- 5.3 Average Transport Cost
SELECT
    AVG(transport_cost) AS avg_transport_cost
FROM supply_chain;
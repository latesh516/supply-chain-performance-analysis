/* =========================================================
   1. INVENTORY TURNOVER
   Measures how quickly inventory is sold
========================================================= */

SELECT 
    sku,
    SUM(products_sold) AS total_sales,
    AVG(stock_level) AS avg_stock,
    SUM(products_sold)*1.0 / NULLIF(AVG(stock_level),0) AS inventory_turnover
FROM supply_chain
GROUP BY sku
ORDER BY inventory_turnover DESC;

/* =========================================================
   2. STOCKOUT RISK PRODUCTS
   Low stock but high demand items
========================================================= */

SELECT sku,
product_type,
stock_level,
products_sold
FROM supply_chain
WHERE stock_level<10
AND products_sold>(SELECT AVG(products_sold) FROM supply_chain)
ORDER BY products_sold DESC;

/* =========================================================
   3. DEMAND VS STOCK GAP
   Identifies demand exceeding inventory
========================================================= */

SELECT sku,
products_sold-stock_level AS demand_stock_gap
FROM supply_chain
ORDER BY demand_stock_gap DESC;

/* =========================================================
   4. EXCESS INVENTORY
   High stock but low demand products
========================================================= */

SELECT
sku,
product_type,
stock_level,
products_sold
FROM supply_chain
WHERE stock_level >
(
SELECT AVG(stock_level) FROM supply_chain
)
AND products_sold <
(
SELECT AVG(products_sold) FROM supply_chain
);

/* =========================================================
   5. AVERAGE STOCK BY PRODUCT TYPE
   Inventory distribution across categories
========================================================= */

SELECT product_type,
AVG(stock_level) AS avg_stock_level
FROM supply_chain
GROUP BY product_type
ORDER BY avg_stock_level DESC;
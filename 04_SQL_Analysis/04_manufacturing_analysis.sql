/* =========================================================
   MANUFACTURING PERFORMANCE ANALYSIS
   Evaluates production volume, manufacturing lead time,
   defect rates, inspection results, and manufacturing cost
========================================================= */

/* =========================================================
   1. PRODUCTION VOLUME BY PRODUCT TYPE
   Measures total production output for each product category
========================================================= */

SELECT
    product_type,
    SUM(production_volume) AS total_production
FROM supply_chain
GROUP BY product_type
ORDER BY total_production DESC;

/* =========================================================
   2. MANUFACTURING LEAD TIME BY PRODUCT TYPE
   Identifies production cycle duration for each category
========================================================= */

SELECT
    product_type,
    AVG(manufacturing_lead_time_days) AS avg_manufacturing_lead_time
FROM supply_chain
GROUP BY product_type
ORDER BY avg_manufacturing_lead_time DESC;

/* =========================================================
   3. DEFECT RATE BY PRODUCT TYPE
   Evaluates product quality performance
========================================================= */

SELECT
    product_type,
    AVG(defect_rate) AS avg_defect_rate
FROM supply_chain
GROUP BY product_type
ORDER BY avg_defect_rate DESC;

/* =========================================================
   4. INSPECTION RESULT DISTRIBUTION
   Shows quality inspection outcomes
========================================================= */

SELECT
    inspection_result,
    COUNT(*) AS total_records
FROM supply_chain
GROUP BY inspection_result;

/* =========================================================
   5. MANUFACTURING COST BY PRODUCT TYPE
   Measures average production cost across product categories
========================================================= */

SELECT
    product_type,
    AVG(manufacturing_cost) AS avg_manufacturing_cost
FROM supply_chain
GROUP BY product_type
ORDER BY avg_manufacturing_cost DESC;
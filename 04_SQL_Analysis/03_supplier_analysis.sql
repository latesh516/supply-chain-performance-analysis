/* =========================================================
   SUPPLIER PERFORMANCE ANALYSIS
   Evaluates supplier efficiency, production contribution,
   logistics cost, and product quality.
========================================================= */


/* =========================================================
   1. SUPPLIER LEAD TIME PERFORMANCE
   Identifies suppliers with longer delivery times
========================================================= */

SELECT
    supplier_name,
    AVG(supplier_lead_time) AS avg_supplier_lead_time
FROM supply_chain
GROUP BY supplier_name
ORDER BY avg_supplier_lead_time DESC;

/* =========================================================
   2. SUPPLIER PRODUCTION CONTRIBUTION
   Measures total production supplied by each supplier
========================================================= */

SELECT
    supplier_name,
    SUM(production_volume) AS total_production
FROM supply_chain
GROUP BY supplier_name
ORDER BY total_production DESC;

/* =========================================================
   3. SUPPLIER SHIPPING COST IMPACT
   Evaluates logistics cost associated with each supplier
========================================================= */

SELECT
    supplier_name,
    AVG(shipping_cost) AS avg_shipping_cost
FROM supply_chain
GROUP BY supplier_name
ORDER BY avg_shipping_cost DESC;

/* =========================================================
   4. SUPPLIER DEFECT RATE ANALYSIS
   Measures product quality issues from suppliers
========================================================= */

SELECT
    supplier_name,
    AVG(defect_rate) AS avg_defect_rate
FROM supply_chain
GROUP BY supplier_name
ORDER BY avg_defect_rate DESC;
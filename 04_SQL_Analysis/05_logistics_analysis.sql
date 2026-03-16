/* =========================================================
   LOGISTICS PERFORMANCE ANALYSIS
   Evaluates shipping carriers, transportation modes,
   and route cost efficiency
========================================================= */


/* =========================================================
   1. SHIPPING COST BY CARRIER
========================================================= */

SELECT
shipping_carrier,
AVG(shipping_cost) AS avg_shipping_cost
FROM supply_chain
GROUP BY shipping_carrier
ORDER BY avg_shipping_cost DESC;

/* =========================================================
   2. SHIPPING TIME BY CARRIER
========================================================= */

SELECT
    shipping_carrier,
    AVG(shipping_time) AS avg_shipping_time
FROM supply_chain
GROUP BY shipping_carrier
ORDER BY avg_shipping_time DESC;

/* =========================================================
   3. TRANSPORT COST BY MODE
========================================================= */

SELECT
    transportation_mode,
    AVG(transport_cost) AS avg_transport_cost
FROM supply_chain
GROUP BY transportation_mode
ORDER BY avg_transport_cost DESC;

/* =========================================================
   4. ROUTE COST ANALYSIS
========================================================= */

SELECT
    route,
    AVG(transport_cost) AS avg_route_cost
FROM supply_chain
GROUP BY route
ORDER BY avg_route_cost DESC;
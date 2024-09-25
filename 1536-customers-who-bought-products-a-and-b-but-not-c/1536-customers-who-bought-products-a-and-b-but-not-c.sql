# Write your MySQL query statement below
SELECT DISTINCT c.customer_id, c.customer_name
FROM Customers c
JOIN Orders oA ON c.customer_id = oA.customer_id AND oA.product_name = 'A'
JOIN Orders oB ON c.customer_id = oB.customer_id AND oB.product_name = 'B'
LEFT JOIN Orders oC ON c.customer_id = oC.customer_id AND oC.product_name = 'C'
WHERE oC.customer_id IS NULL
ORDER BY c.customer_id;


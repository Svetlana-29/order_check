-- Задание 1--
SELECT "Couriers"."login",
    COUNT("Orders"."inDelivery")
FROM "Couriers"
    JOIN "Orders" ON "Couriers"."id" = "Orders"."courierId"
WHERE "Orders"."inDelivery" = true
GROUP BY "Couriers"."login";


--Задание 2--
SELECT "Orders"."track",
    CASE
        WHEN "Orders"."finished" = true THEN 2
        WHEN "Orders"."cancelled" = true THEN -1
        WHEN "Orders"."inDelivery" = true THEN 1
        ELSE 0
    END
FROM "Orders";

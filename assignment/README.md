# Question 1

# Question 2

# Question 3

SELECT
count(1)
FROM green_taxi_data
WHERE lpep_pickup_datetime >= '2025-11-01' AND 
lpep_pickup_datetime < '2025-12-01' AND
trip_distance <= 1;

ANSWER: 8007

# Question 4

SELECT 
lpep_pickup_datetime::date as pickup_day,
trip_distance
FROM green_taxi_data
WHERE trip_distance < 100
ORDER BY trip_distance DESC
LIMIT 1;

ANSWER: Day: 2025-11-14, Trip_distance: 88.03

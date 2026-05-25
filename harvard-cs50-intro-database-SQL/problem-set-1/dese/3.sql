SELECT ROUND(AVG("per_pupil_expenditure"), 2) AS "Average Distric Per-Pupil Expenditure"
FROM "expenditures" GROUP BY "per_pupil_expenditures";
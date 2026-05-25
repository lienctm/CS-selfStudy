-- ** NEED CHECK: It has 68 school district but correct is 65 ** --
SELECT "name", "per_pupil_expenditure", "exemplary" 
FROM "districts"
FROM "districts"
JOIN "expenditures" ON "expenditures"."district_id" = "districts"."id"
JOIN "staff_evaluations" ON "staff_evaluations"."district_id" = "districts"."id"
WHERE "per_pupil_expenditure" > (
    SELECT AVG("per_pupil_expenditure") FROM "expenditures"
) AND "exemplary" > (
    SELECT AVG("exemplary") FROM "staff_evaluations"
) 
ORDER BY "exemplary" DESC, "per_pupil_expenditure" DESC;
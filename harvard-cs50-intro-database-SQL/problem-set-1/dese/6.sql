-- ** NEED CHECK WHY NOT WORKING ** --
--SELECT "name" FROM "schools" WHERE "id" = (
--    SELECT "school_id" FROM "graduation_rates" WHERE "graduated" = 100
--);

-- ** CORRECT ** --
SELECT "name" FROM "schools" JOIN graduation_rates ON
schools.id = graduation_rates.school_id WHERE graduation_rates.graduated = 100;
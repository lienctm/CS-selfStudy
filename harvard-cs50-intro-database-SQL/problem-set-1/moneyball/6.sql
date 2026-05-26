-- ** NEED CHECK: PRINT NOTHING ** --
SELECT "name", SUM("H") AS "total hits"
FROM "teams" JOIN "performances" ON "performances"."id" = "teams"."id"
WHERE "performances"."year" = 2001
ORDER BY "total hits" DESC LIMIT 5;
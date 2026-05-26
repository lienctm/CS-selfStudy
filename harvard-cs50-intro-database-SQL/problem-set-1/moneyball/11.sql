-- ** NEED CHECK: it should print 10 rows while current output is just 1 row ** --
SELECT "first_name", "last_name", SUM("salary") / "H" AS "dollars per hit"
FROM "players"
JOIN "performances" ON "performances"."player_id" = "players"."id"
JOIN "salaries" ON "salaries"."team_id" = "players"."id"
WHERE "H" != 0 AND "performances"."year" = 2001
ORDER BY "dollars per hit" ASC, "first_name" ASC, "last_name" ASC
LIMIT 10;

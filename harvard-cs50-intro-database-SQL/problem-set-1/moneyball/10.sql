SELECT "first_name", "last_name", "salary", "salaries"."year", "HR"
FROM "players" JOIN "salaries" ON "salaries"."player_id" = "players"."id"
JOIN "performances" ON "performances"."player_id" = "players"."id"
WHERE "salaries"."year" = "performances"."year"
ORDER BY "players"."id" ASC, "HR" DESC, "salary" DESC;
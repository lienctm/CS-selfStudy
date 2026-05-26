-- ** NEED CHECK ** --
-- current query's output is 1 but need 3 (team_id = 46,120,64)
SELECT "name" FROM "teams"
WHERE "id" = (
    SELECT DISTINCT("team_id") FROM "performances"
    JOIN "players" ON "players"."id" = "performances"."player_id"
    WHERE "first_name" = 'Satchel' AND "last_name" = 'Paige'
);

SELECT "first_name" AS "left-hand players" FROM "players" 
WHERE "first_name" IS NOT NULL AND "id" > 100 OR "birth_year" < '1988%' 
ORDER BY "last_name" ASC LIMIT 10;
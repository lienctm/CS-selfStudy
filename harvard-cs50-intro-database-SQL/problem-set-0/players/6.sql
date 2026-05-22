SELECT "first_name", "last_name", "debut" FROM "players" 
WHERE "first_name" IS NOT NULL AND "birth_city" = 'Pittsburgh' 
AND "birth_state" = 'PA' ORDER BY "first_name", "last_name", "debut" DESC;
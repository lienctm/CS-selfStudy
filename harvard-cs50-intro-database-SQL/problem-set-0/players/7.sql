SELECT COUNT("id") AS "players" FROM "players" 
WHERE "bats" = 'R' OR 'L' AND "throws" = 'R' OR 'L';
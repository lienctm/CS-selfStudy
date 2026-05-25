SELECT "city", COUNT("name") AS "number of schools" FROM "schools"  WHERE "type" = 'Public School' GROUP BY "city"
ORDER BY "number of schools" DESC, "city" ASC LIMIT 10;
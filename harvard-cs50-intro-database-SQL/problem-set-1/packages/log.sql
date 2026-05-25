
-- *** The Lost Letter ***
-- Find id of addresses
SELECT "id" FROM "addresses" WHERE "address" = '900 Somerville Avenue';
-- Find the wrong address
SELECT "id" FROM "addresses" WHERE "address" LIKE '2 F%Street';
-- Find id, content of the package was sent from Anneke
SELECT "id", "contents" FROM "packagese"
WHERE "from_address_id" = 432 AND "to_address_id" = 854;
-- Check status of the package
SELECT "package_id", "address_id", "action", "timestamp" FROM "scans"
WHERE "package_id" = 384;

-- *** The Devious Delivery ***
-- Find the id of the package where from_address_id IS NULL
SELECT "id" FROM "packages" WHERE "from_address_id" IS NULL;
-- Check if the content of the package is something like what is describe
SELECT "id", "contents" FROM "packages" WHERE "id" = 5098;
-- Find the address
SELECT "address" FROM "addresses" WHERE "id" = (
    SELECT "address_id" FROM "scans" WHERE "package_id" = 5098
);

-- *** The Forgotten Gift ***
-- Find id, content of the package that send from the address 109 Tileston Street
SELECT "id", "contents" FROM "packages" WHERE "from_address_id" = (
    SELECT "id" FROM "addresses" WHERE "address" = '109 Tileston Street'
);




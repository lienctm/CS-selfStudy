CREATE TABLE "passengers" (
    "id" INTEGER,
    "first_name" TEXT NOT NULL,
    "last_name" TEXT NOT NULL,
    "age" INTEGER,
    PRIMARY KEY ("id")
);

CREATE TABLE "check_ins" (
    "check_in_id" INTEGER,
    "passenger_id" INTEGER,
    "datetime" NUMERIC NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "flight" TEXT NOT NULL UNIQUE,
    PRIMARY KEY ("check_in_id"),
    FOREIGN KEY ("passenger_id") REFERENCES "passengers"("id")
);

CREATE TABLE "airlines" (
    "airline_id" INTEGER,
    "name" TEXT NOT NULL UNIQUE,
    "concourse" TEXT NOT NULL CHECK ("concourse" IN ('A', 'B', 'C', 'D', 'T')),
    PRIMARY KEY ("airline_id")
);

CREATE TABLE "flights" (
    "id" INTEGER,
    "number" INTEGER NOT NULL,
    "airline_id" INTEGER,
    "passenger_id" INTEGER,
    "departure" TEXT NOT NULL,
    "destination" TEXT NOT NULL,
    "takeoff_time" NUMERIC NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "arrival_time" NUMERIC NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY ("airline_id") REFERENCES "airlines"("airline_id"),
    FOREIGN KEY ("passenger_id") REFERENCES "passengers"("id")
);
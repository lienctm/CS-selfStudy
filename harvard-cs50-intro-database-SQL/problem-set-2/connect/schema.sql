CREATE TABLE "users" (
    "id" INTEGER,
    "first_name" TEXT NOT NULL,
    "last_name" TEXT NOT NULL,
    "username" TEXT NOT NULL UNIQUE,
    "password" NUMERIC NOT NULL,
    PRIMARY KEY ("id")
);

CREATE TABLE "schools" (
    "id" INTEGER,
    "user_id" INTEGER,
    "school_name" TEXT NOT NULL UNIQUE,
    "school_type" TEXT NOT NULL,
    "location" TEXT NOT NULL,
    "year" INTEGER,
    PRIMARY KEY ("id")
);

CREATE TABLE "companies" (
    "company_id" INTEGER,
    "user_id" INTEGER,
    "name" TEXT NOT NULL UNIQUE,
    "company_type" TEXT NOT NULL,
    "location" TEXT NOT NULL,
    PRIMARY KEY ("company_id")
);

CREATE TABLE "connections" (
    "connection_id" INTEGER,
    "user_id" INTEGER,
    "company_id" INTEGER,
    "school_id" INTEGER,
    "degree" TEXT NOT NULL,
    "degree_start_date" NUMERIC NOT NULL,
    "degree_end_date" NUMERIC NOT NULL,
    "title" TEXT NOT NULL

    PRIMARY KEY ("connection_id"),
    FOREIGN KEY ("user_id") REFERENCES "users"("id"),
    FOREIGN KEY ("company_id") REFERENCES "companies"("company_id")
);
CREATE TABLE users (
    "id" INTEGER,
    "first_name" TEXT NOT NULL,
    "last_name" TEXT NOT NULL,
    "username" TEXT NOT NULL UNIQUE,
    "password" TEXT NOT NULL,
    PRIMARY KEY ("id")
);

CREATE TABLE schools (
    "id" INTEGER,
    "school_name" TEXT NOT NULL UNIQUE,
    "school_type" TEXT NOT NULL,
    "location" TEXT NOT NULL,
    "year" INTEGER,
    PRIMARY KEY ("id")
);

CREATE TABLE companies (
    "company_id" INTEGER,
    "name" TEXT NOT NULL UNIQUE,
    "company_type" TEXT NOT NULL,
    "location" TEXT NOT NULL,
    PRIMARY KEY ("company_id")
);

CREATE TABLE connections (
    "user_id_1" INTEGER,
    "user_id_2" INTEGER,
    "status" TEXT NOT NULL CHECK("status" IN ('pending', 'following')),
    PRIMARY KEY ("user_id_1", "user_id_2"),
    FOREIGN KEY ("user_id_1") REFERENCES "users"("id"),
    FOREIGN KEY ("user_id_2") REFERENCES "users"("id")
);

CREATE TABLE users_schools (
    "id" INTEGER,
    "user_id" INTEGER NOT NULL,
    "school_id" INTEGER NOT NULL,
    "degree" TEXT NOT NULL,
    "degree_start_date" TEXT NOT NULL,
    "degree_end_date" TEXT,
    PRIMARY KEY ("id"),
    FOREIGN KEY ("user_id") REFERENCES "users"("id"),
    FOREIGN KEY ("school_id") REFERENCES "schools"("id")
);

CREATE TABLE users_companies (
    "id" INTEGER,
    "user_id" INTEGER NOT NULL,
    "company_id" INTEGER NOT NULL,
    "job_title" TEXT ,
    "job_start_date" TEXT NOT NULL,
    "job_end_date" TEXT,
    PRIMARY KEY ("id"),
    FOREIGN KEY ("user_id") REFERENCES "users"("id"),
    FOREIGN KEY ("company_id") REFERENCES "companies"("company_id")
);
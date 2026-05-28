CREATE TABLE ingredents (
    "id" INTEGER,
    "type" TEXT NOT NULL,
    "unit" TEXT NOT NULL,
    "price_per_unit" TEXT NOT NULL,
    PRIMARY KEY ("id")
);

CREATE TABLE donuts (
    "id" INTEGER,
    "name" TEXT NOT NULL UNIQUE,
    "gluten_free" TEXT NOT NULL CHECK("gluten_free" IN ('yes', 'no')),
    "price" REAL NOT NULL,
    "ingredent_id" INTEGER NOT NULL,
    PRIMARY KEY ("id"),
    FOREIGN KEY ("ingredent_id") REFERENCES "ingredents"("id")
);

CREATE TABLE orders (
    "order_number" INTEGER,
    "donut_id" TEXT NOT NULL,
    "customer_id" INTEGER,
    PRIMARY KEY ("order_number"),
    FOREIGN KEY ("donut_id") REFERENCES "donuts"("id"),
    FOREIGN KEY ("customer_id") REFERENCES "customers"("id")
);

CREATE TABLE customers (
    "id" INTEGER,
    "first_name" TEXT,
    "last_name" TEXT NOT NULL,
    "order_number" INTEGER,
    PRIMARY KEY ("id"),
    FOREIGN KEY ("order_number") REFERENCES "orders"("order_number")
);
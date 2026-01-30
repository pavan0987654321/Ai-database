
import pymysql
import os
import time

def init_db():
    print("Connecting to MySQL...")
    # Connect to MySQL Server (assuming correct credentials from .env or default root/root)
    # We will try to connect without a DB first
    try:
        connection = pymysql.connect(
            host='localhost',
            user='root',
            password='Pavan@2005', # Assuming 'root' based on langchain_helper.py. Modify if needed.
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )
    except pymysql.MySQLError as e:
        with open("db_error.log", "w") as f:
            f.write(f"Error connecting to MySQL: {e}")
        print(f"Error connecting to MySQL. See db_error.log")
        return

    try:
        with connection.cursor() as cursor:
            print("Creating Database...")
            cursor.execute("DROP DATABASE IF EXISTS atliq_tshirts")
            cursor.execute("CREATE DATABASE atliq_tshirts")
            cursor.execute("USE atliq_tshirts")

            print("Creating Tables...")
            # Create t_shirts table
            cursor.execute("""
            CREATE TABLE t_shirts (
                t_shirt_id INT AUTO_INCREMENT PRIMARY KEY,
                brand ENUM('Van Huesen', 'Levi', 'Nike', 'Adidas') NOT NULL,
                color ENUM('Red', 'Blue', 'Black', 'White') NOT NULL,
                size ENUM('XS', 'S', 'M', 'L', 'XL') NOT NULL,
                price INT CHECK (price BETWEEN 10 AND 50),
                stock_quantity INT NOT NULL,
                UNIQUE KEY brand_color_size (brand, color, size)
            );
            """)

            # Create discounts table
            cursor.execute("""
            CREATE TABLE discounts (
                discount_id INT AUTO_INCREMENT PRIMARY KEY,
                t_shirt_id INT NOT NULL,
                pct_discount DECIMAL(5,2) CHECK (pct_discount BETWEEN 0 AND 100),
                FOREIGN KEY (t_shirt_id) REFERENCES t_shirts(t_shirt_id)
            );
            """)

            print("Creating Stored Procedure...")
            # Create Stored Procedure (No DELIMITER needed for pymysql execute)
            procedure_sql = """
            CREATE PROCEDURE PopulateTShirts()
            BEGIN
                DECLARE counter INT DEFAULT 0;
                DECLARE max_records INT DEFAULT 100;
                DECLARE brand ENUM('Van Huesen', 'Levi', 'Nike', 'Adidas');
                DECLARE color ENUM('Red', 'Blue', 'Black', 'White');
                DECLARE size ENUM('XS', 'S', 'M', 'L', 'XL');
                DECLARE price INT;
                DECLARE stock INT;

                -- Seed the random number generator
                SET SESSION rand_seed1 = UNIX_TIMESTAMP();

                WHILE counter < max_records DO
                    -- Generate random values
                    SET brand = ELT(FLOOR(1 + RAND() * 4), 'Van Huesen', 'Levi', 'Nike', 'Adidas');
                    SET color = ELT(FLOOR(1 + RAND() * 4), 'Red', 'Blue', 'Black', 'White');
                    SET size = ELT(FLOOR(1 + RAND() * 5), 'XS', 'S', 'M', 'L', 'XL');
                    SET price = FLOOR(10 + RAND() * 41);
                    SET stock = FLOOR(10 + RAND() * 91);

                    -- Attempt to insert a new record
                    -- Duplicate brand, color, size combinations will be ignored due to the unique constraint
                    BEGIN
                        DECLARE CONTINUE HANDLER FOR 1062 BEGIN END;  -- Handle duplicate key error
                        INSERT INTO t_shirts (brand, color, size, price, stock_quantity)
                        VALUES (brand, color, size, price, stock);
                        SET counter = counter + 1;
                    END;
                END WHILE;
            END
            """
            cursor.execute(procedure_sql)

            print("Populating T-Shirts (Calling SP)...")
            cursor.execute("CALL PopulateTShirts()")

            print("Populating Discounts...")
            discounts_sql = """
            INSERT INTO discounts (t_shirt_id, pct_discount)
            VALUES
            (1, 10.00),
            (2, 15.00),
            (3, 20.00),
            (4, 5.00),
            (5, 25.00),
            (6, 10.00),
            (7, 30.00),
            (8, 35.00),
            (9, 40.00),
            (10, 45.00);
            """
            cursor.execute(discounts_sql)

        connection.commit()
        print("Database Verification:")
        with connection.cursor() as cursor:
            cursor.execute("SELECT COUNT(*) as count FROM t_shirts")
            result = cursor.fetchone()
            print(f"T-Shirts count: {result['count']}")
            
            cursor.execute("SELECT COUNT(*) as count FROM discounts")
            result = cursor.fetchone()
            print(f"Discounts count: {result['count']}")

    finally:
        connection.close()

if __name__ == "__main__":
    init_db()

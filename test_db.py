import pymysql
import os
from dotenv import load_dotenv

load_dotenv()

# Connect WITHOUT specifying database first
DB_CONFIG_NO_DB = {
    'host': os.getenv('DB_HOST', 'localhost'),
    'port': int(os.getenv('DB_PORT', 3306)),
    'user': os.getenv('DB_USER', 'root'),
    'password': os.getenv('DB_PASSWORD', ''),
    'charset': 'utf8mb4',
}

print("Step 1: Testing connection to MySQL server...")
print("-" * 60)

try:
    connection = pymysql.connect(**DB_CONFIG_NO_DB)
    print("✅ Connected to MySQL server!")
    
    with connection.cursor() as cursor:
        # Check if database exists
        cursor.execute("SHOW DATABASES LIKE 'atliq_tshirts'")
        result = cursor.fetchone()
        
        if result:
            print("✅ Database 'atliq_tshirts' exists!")
        else:
            print("❌ Database 'atliq_tshirts' does NOT exist!")
            print("\n💡 Creating database...")
            cursor.execute("CREATE DATABASE IF NOT EXISTS atliq_tshirts")
            print("✅ Database created!")
    
    connection.close()
    
    # Now try to connect to the database
    print("\nStep 2: Connecting to atliq_tshirts database...")
    print("-" * 60)
    
    DB_CONFIG = {
        **DB_CONFIG_NO_DB,
        'database': 'atliq_tshirts'
    }
    
    connection = pymysql.connect(**DB_CONFIG)
    print("✅ Connected to atliq_tshirts database!")
    
    with connection.cursor() as cursor:
        cursor.execute("SHOW TABLES")
        tables = cursor.fetchall()
        
        if len(tables) == 0:
            print("⚠️  No tables found! Database is empty.")
            print("\n💡 You need to run: database/db_setup.sql")
        else:
            print(f"✅ Found {len(tables)} tables:")
            for table in tables:
                print(f"   - {table[0]}")
    
    connection.close()
    print("\n✅ All connection tests passed!")
    
except pymysql.err.OperationalError as e:
    print(f"❌ MySQL Error:")
    print(f"   Code: {e.args[0]}")
    print(f"   Message: {e.args[1]}")
except Exception as e:
    print(f"❌ Error: {e}")
    import traceback
    traceback.print_exc()

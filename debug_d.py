
import pymysql
import sys

def test_conn(host):
    print(f"Testing {host}...", flush=True)
    try:
        connection = pymysql.connect(
            host=host,
            user='root',
            password='root',
            charset='utf8mb4'
        )
        print(f"SUCCESS: Connected to {host}!", flush=True)
        connection.close()
        return True
    except Exception as e:
        print(f"FAILED {host}: {e}", flush=True)
        return False

test_conn('127.0.0.1')

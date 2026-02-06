#!/usr/bin/env python
"""Test if api_server can be imported successfully"""
import sys
print("Python version:", sys.version)
print("Python path:", sys.path)

try:
    print("\n1. Testing basic imports...")
    import flask
    print("   ✓ Flask imported")
    
    import pymysql
    print("   ✓ pymysql imported")
    
    print("\n2. Testing api_server import...")
    import api_server
    print("   ✓ api_server module imported")
    
    print("\n3. Testing app object...")
    print(f"   ✓ app object found: {api_server.app}")
    print(f"   ✓ app type: {type(api_server.app)}")
    
    print("\n✅ All imports successful!")
    
except Exception as e:
    print(f"\n❌ Import failed: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)

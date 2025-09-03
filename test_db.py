#!/usr/bin/env python3
"""Test database setup and API endpoints"""

import sys
import os
import requests
import json
from pathlib import Path

# Add the app directory to the Python path
sys.path.append(str(Path(__file__).parent / "app"))

def test_database():
    """Test database table creation"""
    print("Testing database setup...")
    
    try:
        from db import engine
        from models import Base, User, Stage, Achievement
        from sqlalchemy import inspect
        from sqlalchemy.orm import Session
        
        # Create tables
        print("Creating tables...")
        Base.metadata.create_all(bind=engine)
        
        # Check what tables exist
        inspector = inspect(engine)
        tables = inspector.get_table_names()
        print(f'Available tables: {tables}')
        
        # Test database connection
        with Session(engine) as db:
            user_count = db.query(User).count()
            stage_count = db.query(Stage).count()
            achievement_count = db.query(Achievement).count()
            
            print(f'Users: {user_count}')
            print(f'Stages: {stage_count}')
            print(f'Achievements: {achievement_count}')
            
        print("✅ Database setup successful!")
        return True
        
    except Exception as e:
        print(f"❌ Database error: {e}")
        return False

def test_api_endpoints():
    """Test API endpoints"""
    print("\nTesting API endpoints...")
    
    base_url = "http://localhost:8000"
    
    # Test health endpoint
    try:
        response = requests.get(f"{base_url}/")
        print(f"Health check: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"❌ Health check failed: {e}")
        return False
    
    # Test registration
    try:
        register_data = {
            "username": "testuser123",
            "email": "test123@example.com", 
            "password": "testpass123"
        }
        
        response = requests.post(
            f"{base_url}/api/auth/register",
            json=register_data,
            headers={"Content-Type": "application/json"}
        )
        
        print(f"Registration: {response.status_code}")
        if response.status_code in [200, 201]:
            print("✅ Registration successful!")
            result = response.json()
            print(f"Response: {json.dumps(result, indent=2)}")
        else:
            print(f"❌ Registration failed: {response.text}")
            
    except Exception as e:
        print(f"❌ Registration error: {e}")
    
    # Test login
    try:
        login_data = {
            "username": "testuser123",
            "password": "testpass123"
        }
        
        response = requests.post(
            f"{base_url}/api/auth/login",
            json=login_data,
            headers={"Content-Type": "application/json"}
        )
        
        print(f"Login: {response.status_code}")
        if response.status_code == 200:
            print("✅ Login successful!")
            result = response.json()
            print(f"Response: {json.dumps(result, indent=2)}")
        else:
            print(f"❌ Login failed: {response.text}")
            
    except Exception as e:
        print(f"❌ Login error: {e}")

if __name__ == "__main__":
    print("🧪 Testing AgriPlay Backend")
    print("=" * 40)
    
    # Test database first
    db_ok = test_database()
    
    if db_ok:
        # Test API endpoints
        test_api_endpoints()
    else:
        print("Skipping API tests due to database issues")
    
    print("=" * 40)
    print("🏁 Testing complete")

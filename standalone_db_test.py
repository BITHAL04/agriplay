"""
Standalone database test script
"""
import os
import sys
from pathlib import Path

# Set the database path
DATABASE_URL = "sqlite:///./agriplay.db"

def test_database():
    """Test database creation"""
    from sqlalchemy import create_engine, inspect
    from sqlalchemy.orm import sessionmaker, Session
    
    # Import models
    sys.path.insert(0, str(Path(__file__).parent / "app"))
    from models import Base, User, Stage, Achievement
    
    print("Creating database engine...")
    engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
    
    print("Creating tables...")
    Base.metadata.create_all(bind=engine)
    
    # Check what tables exist
    inspector = inspect(engine)
    tables = inspector.get_table_names()
    print(f'Available tables: {tables}')
    
    # Test database connection
    SessionLocal = sessionmaker(bind=engine)
    with SessionLocal() as db:
        user_count = db.query(User).count()
        stage_count = db.query(Stage).count() 
        achievement_count = db.query(Achievement).count()
        
        print(f'Users: {user_count}')
        print(f'Stages: {stage_count}')
        print(f'Achievements: {achievement_count}')
    
    print("✅ Database test successful!")
    return True

if __name__ == "__main__":
    try:
        test_database()
    except Exception as e:
        print(f"❌ Database test failed: {e}")
        import traceback
        traceback.print_exc()

import os
from dotenv import load_dotenv

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Load environment variables from .env file
load_dotenv()

# Access the environment variables
db_host = os.getenv("DB_HOST_PROD")
db_user = os.getenv("DB_USER_PROD")
db_password = os.getenv("DB_PASSWORD_PROD")
db_name = os.getenv("DB_NAME_PROD")

# db_prod = "mysql://flow_poemoveras:bf3c98845cb1532f6cb23d0b2882a886756ae1cb@olr.h.filess.io:3307/flow_poemoveras"

# SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_name}"
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://sql8706104:crmly5my5J@sql8.freemysqlhosting.net:3306/sql8706104"

engine = create_engine(url=SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


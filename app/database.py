from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.config import settings

# 'postgresql://<username>:<password>@<ip.address/hostname>/<database_name>'

SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Open and close db on demand
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Connect to the db
# while True:
#     try:
#         conn = psycopg2.connect(host='hostname',
#                                 database='database_name',
#                                 user='user',
#                                 password='password',
#                                 cursor_factory=RealDictCursor)
#         cursor = conn.cursor()
#         print("Database connection was Successful...")
#         break

#     except Exception as error:
#         print("Connecting to Database Failed!")
#         print("Error: ",error)
#         time.sleep(2)
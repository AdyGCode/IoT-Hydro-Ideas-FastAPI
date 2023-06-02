from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# DATABASE_URL = "mysql+mysqlconnector://root@localhost:3306" \
#                "/serversiderendering"

DATABASE_URL = "mysql+mysqlconnector://serversiderendering:Password1@localhost:3306" \
               "/serversiderendering"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False,
                            bind=engine)

Base = declarative_base()

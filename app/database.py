from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

# DATABASE_URL = "mysql+mysqlconnector://root:Mysql%40123@localhost/online_test_system"

# engine = create_engine(DATABASE_URL)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Base = declarative_base()


# SQLALCHEMY_DATABASE_URL = (
#     "mysql+mysqlconnector://root:Mysql@123@localhost/online_test_system"
# )
SQLALCHEMY_DATABASE_URL = (
    "mysql+mysqlconnector://root:Mysql%40123@localhost/online_test_system"
)


engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

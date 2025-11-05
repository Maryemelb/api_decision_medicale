from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

#Database setup
Database_url= 'sqlite:///./database.db' 
engine = create_engine(Database_url) 
sessionLocal = sessionmaker(autocommit = False, autoflush= False, bind=engine) 
Base = declarative_base() 
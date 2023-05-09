from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# DATABASE_URL = 'postgresql://am:postgres@localhost:5432/manga'


DATABASE_URL = 'postgresql://default:DLFVdsNhHi09@ep-wandering-queen-159739.ap-southeast-1.postgres.vercel-storage.com:5432/verceldb'

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

import pandas as pd
from sqlalchemy import create_engine

DB_USER = os.getenv("DB_USER")  # will raise error if not set!!!
DB_PASS = os.getenv("DB_PASS")  # will raise error if not set!!!
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_NAME = os.getenv("DB_NAME", "movies")

# load CSV
df = pd.read_csv("../data/movies.csv")

# connect
engine = create_engine(f"postgresql://{DB_USER}@{DB_HOST}:{DB_PORT}/{DB_NAME}")

# load to db
df.to_sql("movies_raw", engine, if_exists="replace", index=False)

print("Data successfully loaded into 'movies_raw'")
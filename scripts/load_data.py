import pandas as pd
from sqlalchemy import create_engine

# Update with your macOS username
DB_USER = os.getenv("DB_USER", "ltrosas")
DB_PASS = os.getenv("DB_PASS")  # Will raise error if not set
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_NAME = os.getenv("DB_NAME", "movies")

# Load CSV
df = pd.read_csv("../data/movies.csv")

# Connect to PostgreSQL
engine = create_engine(f"postgresql://{DB_USER}@{DB_HOST}:{DB_PORT}/{DB_NAME}")

# Load to PostgreSQL
df.to_sql("movies_raw", engine, if_exists="replace", index=False)

print("Data successfully loaded into 'movies_raw'")
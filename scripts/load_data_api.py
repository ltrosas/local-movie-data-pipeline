import pandas as pd
from sqlalchemy import create_engine
import requests
import os
from dotenv import load_dotenv

load_dotenv()

DB_USER = os.getenv("DB_USER")  # will raise error if not set!!!
DB_PASS = os.getenv("DB_PASS")  # will raise error if not set!!!
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

api_key = os.getenv("IMDB_API_KEY")

# test movies
movies = ["Inception", "The Matrix", "Interstellar"]

movies_data = []

# data for each movie
for movie in movies:
    url = f"http://www.omdbapi.com/?t={movie}&apikey={api_key}"
    response = requests.get(url)
    data = response.json()

    # only add the movie if it was found
    if data["Response"] == "True":
        info = {
            "id": data["imdbID"],
            "title": data["Title"],
            "year": data["Year"],
            "released": data["Released"],
            "country": data["Country"],
            "runtime": data["Runtime"],
            "genre": data["Genre"],
            "director": data["Director"],
            "actors": data["Actors"]
        }
        movies_data.append(info)

df = pd.DataFrame(movies_data)

# load to db
engine = create_engine(f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}")
df.to_sql("movies_raw_api", engine, if_exists="replace", index=False)

print("✅ sucessful")
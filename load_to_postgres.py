import psycopg2
import pandas as pd

# Read processed dataset
data = pd.read_csv("processed_movie_tags.csv")

# Connect to PostgreSQL
conn = psycopg2.connect(
    host="localhost",
    database="moviedb",
    user="postgres",
    password="kavi274"
)

cursor = conn.cursor()

# Insert data row by row
for index, row in data.iterrows():
    cursor.execute(
        "INSERT INTO movie_tags (movieId, title, genres, userId, tag, timestamp) VALUES (%s,%s,%s,%s,%s,%s)",
        (row["movieId"], row["title"], row["genres"], row["userId"], row["tag"], row["timestamp"])
    )

# Save changes
conn.commit()

cursor.close()
conn.close()

print("Data successfully loaded into PostgreSQL!")
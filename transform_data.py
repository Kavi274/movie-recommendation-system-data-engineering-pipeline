import pandas as pd

# Read downloaded CSV files
movie = pd.read_csv("movie.csv")
tag = pd.read_csv("tag.csv")
link = pd.read_csv("link.csv")
genome_tags = pd.read_csv("genome_tags.csv")

# -------------------------------
# 1 Remove duplicate records
# -------------------------------
tag = tag.drop_duplicates()

# -------------------------------
# 2 Convert timestamp to datetime
# -------------------------------
tag['timestamp'] = pd.to_datetime(tag['timestamp'], unit='s')

# -------------------------------
# 3 Handle missing values
# -------------------------------
tag = tag.dropna()

# -------------------------------
# 4 Join movies + tags
# -------------------------------
movie_tag = pd.merge(movie, tag, on="movieId", how="inner")

# -------------------------------
# 5 Preview cleaned data
# -------------------------------
print("Cleaned Dataset Preview:")
print(movie_tag.head())

# -------------------------------
# 6 Save processed dataset
# -------------------------------
movie_tag.to_csv("processed_movie_tags.csv", index=False)

print("Transformation completed successfully!")
import boto3
import pandas as pd

s3 = boto3.client("s3")

bucket = "movie-recommandation-system-raw"

# download files locally
s3.download_file(bucket, "movie.csv", "movie.csv")
s3.download_file(bucket, "tag.csv", "tag.csv")
s3.download_file(bucket, "link.csv", "link.csv")
s3.download_file(bucket, "genome_tags.csv", "genome_tags.csv")

# read locally
movie = pd.read_csv("movie.csv")
tag = pd.read_csv("tag.csv")
link = pd.read_csv("link.csv")
genome_tags = pd.read_csv("genome_tags.csv")

print(movie.head())
print(tag.head())
print(link.head())
print(genome_tags.head())
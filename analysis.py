import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Load data
ratings = pd.read_csv("ratings.csv")
movies = pd.read_csv("movies.csv")
tags = pd.read_csv("tags.csv")

# Step 2: Explore data
print(ratings.head())
print(movies.head())
print(tags.head())

# Step 3: Average ratings per movie
avg_ratings = ratings.groupby("movieId")["rating"].mean().reset_index()
movie_ratings = movies.merge(avg_ratings, on="movieId")

# Top 10 movies by rating
top_movies = movie_ratings.sort_values("rating", ascending=False).head(10)

plt.figure(figsize=(10,6))
sns.barplot(x="rating", y="title", data=top_movies, palette="viridis")
plt.title("Top 10 Highest Rated Movies")
plt.xlabel("Average Rating")
plt.ylabel("Movie Title")
plt.show()

# Step 4: Distribution of ratings
plt.figure(figsize=(8,5))
sns.histplot(ratings["rating"], bins=10, kde=True, color="skyblue")
plt.title("Distribution of Movie Ratings")
plt.xlabel("Rating")
plt.ylabel("Count")
plt.show()
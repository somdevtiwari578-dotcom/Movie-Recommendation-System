import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import streamlit as st
import requests

# -----------------------------
# Load Dataset
# -----------------------------
movies = pd.read_csv("movies.csv")
ratings = pd.read_csv("ratings.csv")

# -----------------------------
# Content-Based Filtering
# -----------------------------
movies['genres'] = movies['genres'].fillna('')
count_vectorizer = CountVectorizer(tokenizer=lambda x: x.split('|'))
genre_matrix = count_vectorizer.fit_transform(movies['genres'])
cosine_sim = cosine_similarity(genre_matrix, genre_matrix)

def content_recommend(movie_title, n=5):
    if movie_title not in movies['title'].values:
        return []
    idx = movies[movies['title'] == movie_title].index[0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:n+1]
    movie_indices = [i[0] for i in sim_scores]
    return movies['title'].iloc[movie_indices].tolist()

# -----------------------------
# Collaborative Filtering (Simple User-Item Average)
# -----------------------------
def collaborative_recommend(user_id, n=5):
    avg_ratings = ratings.groupby("movieId")["rating"].mean()
    user_movies = ratings[ratings["userId"] == user_id]["movieId"].tolist()
    recommendations = avg_ratings.drop(user_movies).sort_values(ascending=False).head(n)
    return movies[movies["movieId"].isin(recommendations.index)]["title"].tolist()

# -----------------------------
# Hybrid Recommendation
# -----------------------------
def hybrid_recommend(movie_title, user_id, n=5):
    content_recs = content_recommend(movie_title, n)
    collab_recs = collaborative_recommend(user_id, n)
    hybrid = list(set(content_recs + collab_recs))
    return hybrid[:n]

# -----------------------------
# TMDb API Integration (Optional)
# -----------------------------
TMDB_API_KEY = "YOUR_API_KEY_HERE"  # <-- apna API key dalna optional hai

def get_movie_details(title):
    url = f"https://api.themoviedb.org/3/search/movie?api_key={TMDB_API_KEY}&query={title}"
    try:
        response = requests.get(url, timeout=5)
        data = response.json()
        if data['results']:
            movie = data['results'][0]
            poster = f"https://image.tmdb.org/t/p/w500{movie['poster_path']}" if movie['poster_path'] else None
            rating = movie.get('vote_average', 'N/A')
            return poster, rating
    except requests.exceptions.RequestException:
        # Agar API connect na ho to safe fallback
        return None, None
    return None, None

# -----------------------------
# Streamlit UI
# -----------------------------
st.title("🎬 Hybrid Movie Recommendation System")

movie_name = st.text_input("Enter a movie name:")
user_id = st.number_input("Enter your User ID:", min_value=1, step=1)

if st.button("Recommend"):
    recommendations = hybrid_recommend(movie_name, user_id)
    if recommendations:
        st.write("Recommended Movies:")
        for rec in recommendations:
            poster, rating = get_movie_details(rec)
            st.subheader(rec)
            if poster:
                st.image(poster, width=150)
            else:
                st.write("Poster not available")
            st.write(f"⭐ Rating: {rating if rating else 'N/A'}")
    else:
        st.write("No recommendations found. Try another movie or user ID.")
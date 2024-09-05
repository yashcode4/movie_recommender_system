import streamlit as st
import pickle
import requests

def fetch_poster(movie_title):
    response = requests.get('https://www.omdbapi.com/?t={}&apikey=15242e22'.format(movie_title))
    data = response.json()
    return data['Poster']

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    movies_list = similarity[movie_index]

    recommended_movies = []
    recommend_movies_posters = []

    for i in movies_list:
        movie_title = movies.iloc[i[0]].title
        # fetch movie title from movie.pkl file
        recommended_movies.append(movie_title)
        # fetch poster from API
        recommend_movies_posters.append(fetch_poster(movie_title))

    return recommended_movies, recommend_movies_posters

movies = pickle.load(open('models/movies.pkl', 'rb'))
similarity = pickle.load(open('models/reduced_similarity.pkl', 'rb'))

st.set_page_config(page_title="Movie Recommender System")

st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
    "Choose Movie...",
    movies['title'].values)

if st.button("Recommend"):
    names, posters = recommend(selected_movie_name)
    
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])

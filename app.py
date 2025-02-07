import streamlit as st
import pickle
import pandas as pd


def recommend(movie):
    movies.loc[:, 'title'] = movies['title'].str.lower()
    movie = movie.lower()
    if movie not in movies['title'].values:
        return [f"The movie '{movie}' is not in the dataset."]

    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommend_movies = [movies.iloc[i[0]]['title'] for i in movies_list]
    return recommend_movies


movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

st.set_page_config(page_title='Movie Recommender System', page_icon='🎬', layout='centered')

st.markdown(
    """
    <style>
    .reportview-container {
        background-color: #ffffff;
    }
    .main {
        font-family: 'Arial', sans-serif;
        background-color: #ffffff;
        padding: 2rem;
        border-radius: 10px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
    }
    .stButton>button {
        background-color: #007bff !important;
        color: white !important;
        padding: 10px 20px;
        border-radius: 8px;
        font-size: 1rem;
        border: none;
    }
    .stButton>button:hover {
        background-color: #0056b3 !important;
    }
    footer {
        font-family: Arial, sans-serif;
        color: #444;
        font-size: 0.9rem;
        text-align: center;
        padding: 12px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title('🎬 Movie Recommender System')

selected_movie_name = st.selectbox(
    'Select a movie you like:',
    movies['title'].values
)

if st.button('Recommend'):
    recommendations = recommend(selected_movie_name)

    st.subheader("Recommended Movies:")
    for movie in recommendations:
        st.markdown(f"✅ **{movie}**")

st.markdown(
    """
    <footer>
        <p>Created ❤️ by Movie Enthusiast</p>
    </footer>
    """,
    unsafe_allow_html=True
)

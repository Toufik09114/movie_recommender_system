import streamlit as st
import pickle
from user_auth import register, login, logout
from utils import recommend
from database import create_db, fetch_history, save_recommendation

# create the database if it does not exist
create_db()

movies = pickle.load(open("movies_list.pkl", "rb"))
similarity = pickle.load(open("similarity.pkl", 'rb'))

movies_list = movies['title'].values

st.title("Movie Recommender System")
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

if st.session_state.logged_in:
    # Navigation Menu
    page = st.sidebar.radio('Navigation', ["Recommendation", 'Recommendation History'])

    if st.sidebar.button('Logout'):
        logout()
        st.session_state.logged_in = False
        st.rerun()

    if page == 'Recommendation':
        selected_movies_name = st.selectbox('Need recommendation for movies?', movies_list)

        if st.button('Recommend'):
            names, posters, descriptions, ratings, genres_list, similarity_scores, trailers_list, actors_list, directors_list = recommend(
                selected_movies_name, movies, similarity)

            for i in range(len(names)):
                with st.container():
                    col1, col2 = st.columns([1, 4])
                    with col1:
                        st.image(posters[i])
                    with col2:
                        st.subheader(names[i])
                        st.text(f'Rating: {ratings[i]}')
                        st.text(f'Genres: {", ".join(genres_list[i])}')
                        st.text(f'Similarity score: {similarity_scores[i]:.2f}%')
                        st.text(f'Overview: {descriptions[i]}')

                        if trailers_list[i]:
                            st.markdown(f'[Watch Trailer]({trailers_list[i]})')

                        if actors_list[i]:
                            st.write('**Actor:**')
                            actor_row = st.columns(len(actors_list[i]))
                            for actor, actor_col in zip(actors_list[i], actor_row):
                                actor_col.info(actor)

                        if directors_list[i]:
                            st.write("**Directors:**")
                            director_row = st.columns(len(directors_list[i]))
                            for director, director_col in zip(directors_list[i], director_row):
                                director_col.success(director)

                        st.markdown('----')
                save_recommendation(st.session_state.user_id, movies.iloc[i].movie_id, names[i])

    elif page == 'Recommendation History':
        st.subheader("Your Recommended History")
        history = fetch_history(st.session_state.user_id)
        unique_movies = {}
        for record in history:
            if record[0] not in unique_movies:
                unique_movies[record[0]] = record[1]

        for movie, date in unique_movies.items():
            with st.expander(movie):
                st.write(f'Recommended on: {date}')
else:
    choice = st.sidebar.selectbox('Login/Register', ["Login", "Register"])
    if choice == 'Login':
        login()
    else:
        register()

# def fetch_poster(movie_id):
#     url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US'
#     # request data from url
#     data = requests.get(url)
#     # convert data into json format
#     data = data.json()
#     # extracting poster path
#     poster_path = data['poster_path']
#     # Full path of movie
#     full_path = "https://image.tmdb.org/t/p/w185/" + poster_path
#     return full_path
#
# def recommend(movie):
#     movies_index = movies[movies["title"] == movie].index[0]
#     distance = sorted(list(enumerate(similarity[movies_index])), reverse = True, key=lambda x: x[1])
#     similar_movies = []
#     similar_movies_id = []
#     for i in distance[1:6]:
#         movies_id = i[0]
#         similar_movies.append(movies_list[i[0]])
#         similar_movies_id.append(fetch_poster(movies.iloc[i[0]].movie_id))
#     return similar_movies, similar_movies_id
#
# # Title of the page
# st.title("Recommender System")
#
# # Select box
# movies_list = movies["title"].values
# selected_movie = st.selectbox(
#     "Select a movie from Dropdown",
#     movies_list,
# )
#
# # Recommend Button
# if st.button("Recommend", type="primary"):
#     movies_name, movies_poster = recommend(selected_movie)
#     col1, col2, col3, col4, col5 = st.columns(5)
#
#     with col1:
#          st.image(movies_poster[0])
#          st.text(movies_name[0])
#
#     with col2:
#          st.image(movies_poster[1])
#          st.text(movies_name[1])
#
#     with col3:
#          st.image(movies_poster[2])
#          st.text(movies_name[2])
#
#     with col4:
#          st.image(movies_poster[3])
#          st.text(movies_name[3])
#
#     with col5:
#          st.image(movies_poster[4])
#          st.text(movies_name[4])


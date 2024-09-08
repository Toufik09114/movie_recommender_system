import requests

API_key = 'f95dec74f1d47facce442b391a4b8572'

def fetch_poster(movie_id):
    url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_key}&language=en-US&append_to_response=videos,credits'
    response = requests.get(url)
    data = response.json()
    poster_url = 'https://image.tmdb.org/t/p/w500/'+ data.get('poster_path', '')
    overview = data.get('overview', '')
    rating = data.get('vote_average', 'N/A')
    genres = data.get('genres', [])
    trailers = data.get('videos', {}).get('results', [])
    credits = data.get('credits', {})

    actors = [member['name'] for member in credits.get('cast', [])[:5]]
    directors = [member['name'] for member in credits.get('crew', []) if member['job'] == 'Director']

    trailer_url = None
    for trailer in trailers:
        if trailer['type'] == 'Trailer':
            trailer_url = f"https://www.youtube.com/watch?v={trailer['key']}"
            break
    return poster_url, overview, rating, genres, trailer_url, actors, directors


def recommend(movie_title, movies, similarity):
    movie_index = movies[movies['title'] == movie_title].index[0]
    distances = similarity[movie_index]

    max_distance = max(distances)
    min_distance = min(distances)

    # normalize the score into percentage
    normalize_scores = [(distance - min_distance)/(max_distance - distance)*100 for distance in distances]

    movie_list = sorted(list(enumerate(normalize_scores)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_posters = []
    description = []
    ratings = []
    genres_list = []
    similarity_scores = []
    trailers_list = []
    actors_list = []
    directors_list = []

    for i in movie_list:
        movie_id = movies.iloc[i[0]].movie_id
        title = movies.iloc[i[0]].title

        poster, overview, rating, genres, trailer_url, actors, directors = fetch_poster(movie_id)

        recommended_movies.append(title)
        recommended_movies_posters.append(poster)
        description.append(overview)
        ratings.append(rating)
        genres_list.append([genre['name'] for genre in genres])
        similarity_scores.append(i[1])
        trailers_list.append(trailer_url)
        actors_list.append(actors)
        directors_list.append(directors)

    return recommended_movies, recommended_movies_posters, description, ratings, genres_list, similarity_scores, trailers_list, actors_list, directors_list
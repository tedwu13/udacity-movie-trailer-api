import media
import fresh_tomatoes
import json
import requests

# Shouldn't store API Keys like this. should have an environment file or some sort and port it over to this file
# Capitalize constants for best practices
API_KEY = "0a10838a61551f7017f8992348bfa812"
IMDB_POPULAR_MOVIES_URL = "https://api.themoviedb.org/3/movie/popular?api_key=" + API_KEY


# This function gets a movie url which is a third party api and get the json data for all popular movies
def get_imdb_api(url):
    payload = "{}"
    response = requests.get(IMDB_POPULAR_MOVIES_URL, data=payload)
    return json.loads(response.text).get("results")

# This function calls another trailer api based on the movie id and the response contains an unique youtube key
# This youtube key can be appended to the youtube url to get the actual link of the video
def get_movie_trailer(movie_id):
    trailer_url = "https://api.themoviedb.org/3/movie/" + str(movie_id) + "/videos?api_key=" + API_KEY
    trailer_data = get_imdb_api(trailer_url)
    video_key = trailer_data[0].get("key")
    return "https://www.youtube.com/watch?v=" + str(video_key)


json_data = get_imdb_api(IMDB_POPULAR_MOVIES_URL)
movies = []

# The process is this, first get all the popular movies and then populate the values like title, description, vote averages, release data..etc
# Tricky part is to get the youtube link and calls get_movie_trailer to get the exact movie trailer link
# The idea is to have a movies list and loop through all the results and create a Movie instance and store it into the list
for result in json_data:
    id = result.get("id")
    youtube_link = get_movie_trailer(id)
    title = result.get("title")
    description = result.get("overview")
    image_url = "http://image.tmdb.org/t/p/w185//" + result.get("poster_path")
    vote_average = result.get("vote_average")
    release_date = result.get("release_date")
    popularity = result.get("popularity")
    movie = media.Movie(title, description, image_url, youtube_link, vote_average, release_date, popularity)
    movies.append(movie)


# After that, pass it in as a parameter
fresh_tomatoes.open_movies_page(movies)


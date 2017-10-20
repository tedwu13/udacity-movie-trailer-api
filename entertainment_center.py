import media
import fresh_tomatoes
import json
import requests

# Shouldn't store API Keys like this. should have an environment file or some sort and port it over to this file
# Capitalize constants for best practices
API_KEY = "0a10838a61551f7017f8992348bfa812"
IMDB_POPULAR_MOVIES_URL = "https://api.themoviedb.org/3/movie/popular?api_key=" + API_KEY

def get_imdb_api(url):
    """Fetches movie data from imdb (third party api).

    Retrieves popular movies data from IMDB and uses json python module to convert into JSON format

    Args:
        url: the url that is the third party url

    Returns:
        A dict with multiple keys of all the metadata from the json. Here, we care about results field because that is where all the data is stored
        that is why there is a getter method for the dictionary
    """
    payload = "{}"
    response = requests.get(IMDB_POPULAR_MOVIES_URL, data=payload)
    return json.loads(response.text).get("results")

# This function calls another trailer api based on the movie id and the response contains an unique youtube key
# This youtube key can be appended to the youtube url to get the actual link of the video
def get_movie_trailer(movie_id):
    """Fetches movie trailers keys from movie id

    Retrieves all the videos associated with the movie id

    Args:
        movie_id: the id that is associated with each movie

    Returns:
        A youtube link with the query/key that is associated with the movie
    """
    trailer_url = "https://api.themoviedb.org/3/movie/" + str(movie_id) + "/videos?api_key=" + API_KEY
    trailer_data = get_imdb_api(trailer_url)
    video_key = trailer_data[0].get("key")
    return "https://www.youtube.com/watch?v=" + str(video_key)


json_data = get_imdb_api(IMDB_POPULAR_MOVIES_URL)
movies = []

# First we get all the popular movies and then populate the values like title, description, vote averages, release data..etc
# We construct he youtube link and invokes get_movie_trailer method to get the exact movie trailer link
# Also we create multiple Movie instances dynamically and store it into the movie list

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


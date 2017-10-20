import media
import fresh_tomatoes
import json
import requests


API_KEY = "0a10838a61551f7017f8992348bfa812"
url = "https://api.themoviedb.org/3/movie/popular?api_key=" + API_KEY

def get_imdb_api(url):
    payload = "{}"
    response = requests.get(url, data=payload)
    return json.loads(response.text).get("results")

def get_movie_trailer(movie_id):
    url = "https://api.themoviedb.org/3/movie/" + str(movie_id) + "/videos?api_key=" + API_KEY
    trailer_data = get_imdb_api(url)
    return "https://www.youtube.com/watch?v=" + str(trailer_data[0].get("key"))


json_data = get_imdb_api(url)
movies = []

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



# toy_story = media.Movie("Toy Story",
#                         "A story of a boy and his toys that come to life",
#                         "http://a.dilcdn.com/bl/wp-content/uploads/sites/8/2013/02/toy_story_wallpaper_by_artifypics-d5gss19.jpg",
#                         "https://www.youtube.com/watch?v=SgoiKLFBA3Q")


fresh_tomatoes.open_movies_page(movies)


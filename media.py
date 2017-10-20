import webbrowser
class Movie():
    "This is a Movie Class that has title storyline, poster image, and trailers"
    print __doc__
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]
    def __init__(self, title, description, poster_image_url, trailer_youtube_url, vote_average, release_date, popularity):
        self.title = title
        self.description = description
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
        self.vote_average = vote_average
        self.release_date = release_date
        self.popularity = popularity

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

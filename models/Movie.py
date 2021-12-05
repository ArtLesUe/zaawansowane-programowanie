class Movie:
    def __init__(self, movieId: int, title: str, genres: str) -> None:
        self._movieId = movieId
        self._title = title
        self._genres = genres

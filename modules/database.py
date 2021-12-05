from models.Movie import Movie


def read_movies_from_database() -> list():
    csv = open(file="database/movies.csv", mode="r", encoding="utf8")
    headers = csv.readline().replace('\n', '').split(",")
    movies = list()

    for line in csv.readlines():
        movie = dict()
        for idx, header in enumerate(headers):
            movie[header] = line.split(',')[idx]
        movies.append(Movie(**movie).__dict__)

    csv.close()
    return movies

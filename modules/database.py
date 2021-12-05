def read_movies_from_database() -> list():
    csv = open("database/movies.csv", "r")
    headers = csv.readline().replace('\n', '').split(",")

    for line in csv.readlines():
        print(dict(['a', 'b']))

    csv.close()

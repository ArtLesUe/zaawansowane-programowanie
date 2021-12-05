from models.Movie import Movie


def read_movies_from_database(class_type, file_name: str) -> list():
    csv = open(file=file_name, mode="r", encoding="utf8")
    headers = csv.readline().replace('\n', '').split(",")
    items = list()

    for line in csv.readlines():
        newItem = dict()
        for idx, header in enumerate(headers):
            newItem[header] = line.replace('\n', '').split(',')[idx]
        items.append(class_type(**newItem).__dict__)

    csv.close()
    return items

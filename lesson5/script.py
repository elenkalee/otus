import csv
import json

with open("/lesson5/data/users.json", "r", encoding="utf-8") as f:
    users = json.loads(f.read())

with open("/lesson5/data/books.csv", newline="", encoding="utf-8") as f:
    books = csv.DictReader(f)

    iter_user = iter(users)

    for row in books:
        try:
            current_user = next(iter_user)
        except StopIteration:
            iter_user = iter(users)
            current_user = next(iter_user)

        if "books" not in current_user:
            current_user["books"] = []

        current_user["books"].append({
            "title": row["Title"],
            "author": row["Author"],
            "pages": row["Pages"],
            "genre": row["Genre"],
        })

data = []

for user in users:
    data.append({
        "name": user["name"],
        "gender": user["gender"],
        "address": user["address"],
        "age": user["age"],
        "books": user["books"]
    })

with open('/lesson5/data/result.json', 'w') as f:
    result = json.dumps(data, indent=4)
    f.write(result)

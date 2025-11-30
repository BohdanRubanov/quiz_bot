import json



def json_data():
    with open(file="data/users.json", mode="r") as file:
        users_data: dict = json.load(file)
    return users_data

def save_data(users):
    with open(file="data/users.json", mode="w") as file:
        file.write(json.dumps(users, indent=4, ensure_ascii=False))
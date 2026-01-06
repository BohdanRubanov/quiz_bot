import json



def json_data(file_name: str):
    with open(file=f"data/{file_name}", mode="r") as file:
        users_data: dict = json.load(file)
    return users_data

def save_data(file_name: str, data):
    with open(file=f"data/{file_name}", mode="w") as file:
        file.write(json.dumps(data, indent=4, ensure_ascii=False))
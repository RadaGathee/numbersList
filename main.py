import json
import random
import os

def generate_ids(prefix, count, length):
    return [f"{prefix}{random.randint(10**(length-1), 10**length - 1)}" for _ in range(count)]

def update_json_file(filename, new_ids):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            data = json.load(file)
    else:
        data = []

    data.extend(new_ids)

    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

if __name__ == "__main__":
    prefix = "nambari/"
    count = 20
    length = 8
    filename = "numbersPython_ids.json"

    new_ids = generate_ids(prefix, count, length)
    update_json_file(filename, new_ids)

    print(f"Generated IDs: {new_ids}")

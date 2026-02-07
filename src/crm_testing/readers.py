import json

def read_json_data(json_path):
    """Read and parse JSON data from a file."""
    with open(json_path, 'r') as file:
        data = json.load(file)
    return data

"""This script help us to test json data manipulation using python"""
import json as json
import jq

def validate_json_extension(filename):
    # first we need to check if it is a json file
    if filename.endswith(".json"):
        print(f"{filename} has a valid JSON extension.")
    else:
        print(f"{filename} does not have a valid JSON extension.")

def read_json_data(json_path):
    with open(json_path, 'r') as file:
    # Use json.load() to parse the data from the file object
        data = json.load(file)
        return data

def extract_mails(data):


if __name__ == "__main__":
    data = "/home/fabri/Projects/crm-testing/data/customers.json"
    filename = data
    validate_json_extension(filename)
    my_json_data = read_json_data(data)
    print(my_json_data)

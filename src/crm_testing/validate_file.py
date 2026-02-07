def validate_json_extension(filename):
    if not filename.endswith(".json"):
        raise ValueError(f"{filename} is not a JSON file")
    return filename

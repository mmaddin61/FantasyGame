import json
from exceptions import DialogueDataError
from character import Character

def load_json_data(file_path):
    """Loads the JSON data from the specified file path.
    
    Args:
        file_path (str): The path to the JSON file.

    Returns:
        dict: The JSON data.
    """
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return data
    except:
        raise DialogueDataError("Failed to load the dialogue data.")
    
def parse_characters(data):
    """Parses the characters from the JSON data.
    
    Args:
        data (dict): The JSON data.

    Returns:
        list: Character objects.
    """
    characters = []
    for character in data['characters']:
        characters.append(Character(character['guid'], character['name']))
    return characters
import json
from exceptions import DialogueDataError
from character import Character
from node import Node
from choice import Choice

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

def parse_nodes(data):
    """Parses the nodes from the JSON data.
    
    Args:
        data (dict): The JSON data.

    Returns:
        list: Node objects.
    """
    nodes = []
    for node in data['nodes']:
        nodes.append(Node(node['guid'], node['type'], node['character_guid'], node['choice_guids'], node['label'], node['content']))
    return nodes

def parse_choices(data):
    """Parses the choices from the JSON data.
    
    Args:
        data (dict): The JSON data.

    Returns:
        list: Choice objects.
    """
    choices = []
    for choice in data['choices']:
        choices.append(Choice(choice['guid'], choice['label'], choice['target_node_guid']))
    return choices
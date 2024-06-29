import json
from exceptions import DialogueDataError
#from character import Character
#from node import Node
#from choice import Choice
from character_node import CharacterNode
from dialogue_node import DialogueNode
from choice_node import ChoiceNode
from event_node import EventNode

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
        characters.append(CharacterNode(character['guid'], character['name']))
    return characters

def parse_dialogue(data):
    """Parses the dialogue from the JSON data.
    
    Args:
        data (dict): The JSON data.

    Returns:
        list: Node objects.
    """
    nodes = []
    for node in data['dialogueNodes']:
        nodes.append(DialogueNode(node['guid'], node['characterGuid'], node['label'], node['content'], node['choiceGuids']))
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
        choices.append(ChoiceNode(choice['guid'], choice['parentGuid'], choice['nextGuid'], choice['content']))
    return choices

def parse_events(data):
    """Parses the events from the JSON data.
    
    Args:
        data (dict): The JSON data.

    Returns:
        list: Event objects.
    """
    events = []
    for event in data['eventNodes']:
        print(event)  # Debug line to see the structure of each event
        if 'nextGuid' not in event:
            events.append(EventNode(event['guid'], event['name']))
        else:
            events.append(EventNode(event['guid'], event['name'], event['nextGuid']))
    return events

def parse_root(data):
    """Parses the root node from the JSON data.
    
    Args:
        data (dict): The JSON data.

    Returns:
        Node: The root node.
    """
    root = data['root']
    return DialogueNode(root['guid'], root['characterGuid'], root['label'], root['content'], root['choiceGuids'])
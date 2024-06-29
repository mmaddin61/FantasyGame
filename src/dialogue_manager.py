import data_parser as parser
from character_node import CharacterNode
from choice_node import ChoiceNode
from dialogue_node import DialogueNode
from event_node import EventNode
from exceptions import ElementNotFoundError, ElementExistsError

class DialogueManager:
    def __init__(self):
        self.character_data = []
        self.choice_data = []
        self.dialogue_data = []
        self.event_data = []
        self.character_nodes = {}
        self.choice_nodes = {}
        self.dialogue_nodes = {}
        self.event_nodes = {}
        self.root_node = None
        self.initialized = False

    def initialize(self, data):
        """Initializes the dialogue manager with the JSON data.

        Args:
            data (dict): The JSON data.
        """
        self.character_data = parser.parse_characters(data)
        self.choice_data = parser.parse_choices(data)
        self.dialogue_data = parser.parse_dialogue(data)
        self.event_data = parser.parse_events(data)

        for character in self.character_data:
            self.add_character(character)

        for choice in self.choice_data:
            self.add_choice(choice)

        for dialogue in self.dialogue_data:
            self.add_dialogue(dialogue)

        for event in self.event_data:
            self.add_event(event)

        self.root_node = parser.parse_root(data)

    def has_character(self, guid):
        return guid in self.character_nodes
    def has_choice(self, guid):
        return guid in self.choice_nodes
    def has_dialogue(self, guid):
        return guid in self.dialogue_nodes
    def has_event(self, guid):
        return guid in self.event_nodes
    def is_initialized(self):
        return self.initialized
    
    def get_character(self, guid):
        if self.has_character(guid):
            return self.character_nodes[guid]
        else:
            raise ElementNotFoundError("The character with GUID '" + guid + "' was not found.")
        
    def get_choice(self, guid):
        if self.has_choice(guid):
            return self.choice_nodes[guid]
        else:
            raise ElementNotFoundError("The choice with GUID '" + guid + "' was not found.")
        
    def get_dialogue(self, guid):
        if self.has_dialogue(guid):
            return self.dialogue_nodes[guid]
        else:
            raise ElementNotFoundError("The dialogue with GUID '" + guid + "' was not found.")
        
    def get_event(self, guid):
        if self.has_event(guid):
            return self.event_nodes[guid]
        else:
            raise ElementNotFoundError("The event with GUID '" + guid + "' was not found.")
        
    def get_root(self):
        if self.root_node is not None:
            return self.root_node
        else:
            raise ElementNotFoundError("The root node was not found.")
    
    def add_character(self, character):
        if self.has_character(character.get_guid()):
            raise ElementExistsError("The character with GUID '" + character.get_guid() + "' already exists.")
        else:
            self.character_nodes[character.get_guid()] = character

    def add_choice(self, choice):
        if self.has_choice(choice.get_guid()):
            raise ElementExistsError("The choice with GUID '" + choice.get_guid() + "' already exists.")
        else:
            self.choice_nodes[choice.get_guid()] = choice

    def add_dialogue(self, dialogue):
        if self.has_dialogue(dialogue.get_guid()):
            raise ElementExistsError("The dialogue with GUID '" + dialogue.get_guid() + "' already exists.")
        else:
            self.dialogue_nodes[dialogue.get_guid()] = dialogue

    def add_event(self, event):
        if self.has_event(event.get_guid()):
            raise ElementExistsError("The event with GUID '" + event.get_guid() + "' already exists.")
        else:
            self.event_nodes[event.get_guid()] = event
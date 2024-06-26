class Node:
    def __init__(self, guid, type, character_guid, choice_guids, label='Dialogue Node', content=''):
        self.guid = guid
        self.type = type
        self.character_guid = character_guid
        self.choice_guids = choice_guids
        self.label = label
        self.content = content
        
    def get_guid(self):
        return self.guid
    def get_type(self):
        return self.type
    def get_character_guid(self):
        return self.character_guid
    def get_choice_guids(self):
        return self.choice_guids
    def get_label(self):
        return self.label
    def get_content(self):
        return self.content
from node import Node

class DialogueNode(Node):
    def __init__(self, guid, character_guid, label, content, choice_guids):
        super().__init__(guid, 'DIALOGUE_NODE')
        self.character_guid = character_guid
        self.label = label
        self.content = content
        self.choice_guids = choice_guids

    def get_character_guid(self):
        return self.character_guid
    def get_label(self):
        return self.label
    def get_content(self):
        return self.content
    def get_choice_guids(self):
        return self.choice_guids
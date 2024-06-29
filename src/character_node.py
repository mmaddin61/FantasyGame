from node import Node

class CharacterNode(Node):
    def __init__(self, guid, name):
        super().__init__(guid, 'CHARACTER_NODE')
        self.name = name

    def get_name(self):
        return self.name
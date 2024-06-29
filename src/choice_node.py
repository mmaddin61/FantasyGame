from node import Node

class ChoiceNode(Node):
    def __init__(self, guid, parent_guid, next_guid, content):
        super().__init__(guid, 'CHOICE_NODE')
        self.parent_guid = parent_guid
        self.next_guid = next_guid
        self.content = content

    def get_parent_guid(self):
        return self.parent_guid
    def get_next_guid(self):
        return self.next_guid
    def get_content(self):
        return self.content
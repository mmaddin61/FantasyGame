from node import Node

class EventNode(Node):
    def __init__(self, guid, name, next_guid):
        super().__init__(guid, 'EVENT_NODE')
        self.name = name
        self.next_guid = next_guid

    def get_name(self):
        return self.name
    def get_next_guid(self):
        return self.next_guid
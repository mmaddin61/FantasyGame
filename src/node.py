class Node:
    """Represents a node exported from the dialogue editor."""
    def __init__(self, guid, type_name):
        self.guid = guid
        self.type = type_name

    def get_guid(self):
        return self.guid
    def get_type_name(self):
        return self.type_name
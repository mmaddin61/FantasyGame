class Character:
    def __init__(self, guid, name='Narrator'):
        self.guid = guid
        self.name = name

    def get_guid(self):
        return self.guid
    def get_name(self):
        return self.name
    
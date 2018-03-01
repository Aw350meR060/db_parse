class Index:
    def __init__(self):
        self.name = None
        self.fulltext = False
        self.uniqueness = False
        self.fields = []
        self.is_clustered = False

class Item:
    def __init__(self):
        self.name = None
        self.expression = None
        self.desc = False
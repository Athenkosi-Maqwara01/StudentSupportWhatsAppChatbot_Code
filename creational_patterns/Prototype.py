import copy

class QueryPrototype:
    def __init__(self, query):
        self.query = query

    def clone(self):
        return QueryPrototype(copy.deepcopy(self.query))

class Database:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Database, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self, connection_string):
        if not hasattr(self, 'initialized'):
            self._connection_string = connection_string
            self.initialized = True

from src.Query import Query 
from src.Response import Response
from src.Notification import Notification


class ObjectFactory:
    @staticmethod
    def create_object(object_type, *args, **kwargs):
        if object_type == 'Query':
            return Query(*args, **kwargs)
        elif object_type == 'Response':
            return Response(*args, **kwargs)
        elif object_type == 'Notification':
            return Notification(*args, **kwargs)
        else:
            raise ValueError("Unknown object type")

from abc import ABC, abstractmethod
from src.Query import Query 
from src.Response import Response

class SupportSystemFactory(ABC):
    @abstractmethod
    def create_query(self):
        pass

    @abstractmethod
    def create_response(self):
        pass

class StudentSupportFactory(SupportSystemFactory):
    def create_query(self):
        return Query(query_id=1, content="Help with course material", category="Academic", intent_score=0.8)

    def create_response(self):
        return Response(response_id=1, content="Here is the information on course material.", response_type="Text")

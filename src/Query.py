from enum import Enum
from datetime import datetime

class QueryStatus(Enum):
    NEW = "new"
    IN_PROGRESS = "in_progress"
    ESCALATED = "escalated"
    RESOLVED = "resolved"

class Query:
    def __init__(self, query_id, content, category, intent_score):
        self.__query_id = query_id
        self.__content = content
        self.__timestamp = datetime.now()
        self.__category = category
        self.__status = QueryStatus.NEW
        self.__intent_score = intent_score

    def process(self):
        if self.__intent_score < 0.6:
            self.escalate()
        else:
            self.classify()

    def escalate(self):
        self.__status = QueryStatus.ESCALATED
        print(f"Query {self.__query_id} escalated due to low intent score.")

    def classify(self):
        print(f"Classifying query {self.__query_id} in category '{self.__category}'.")

    def resolveWithResponse(self, response):
        self.__status = QueryStatus.RESOLVED
        print(f"Query {self.__query_id} resolved with response {response.get_response_id()}.")

    # Getters
    def get_query_id(self): return self.__query_id

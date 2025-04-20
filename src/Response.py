from datetime import datetime

class Response:
    def __init__(self, response_id, content, response_type, attachments=[]):
        self.__response_id = response_id
        self.__content = content
        self.__timestamp = datetime.now()
        self.__response_type = response_type
        self.__attachments = attachments
        self.__delivered = False

    def deliver(self):
        self.__delivered = True
        print(f"Response {self.__response_id} delivered.")

    def trackDeliveryStatus(self):
        return self.__delivered

    def recordFeedback(self, feedback):
        print(f"Feedback on response {self.__response_id}: {feedback}")

    def get_response_id(self): return self.__response_id

from datetime import datetime, timedelta

class ChatSession:
    def __init__(self, session_id, channel_type):
        self.__session_id = session_id
        self.__start_time = datetime.now()
        self.__end_time = None
        self.__channel_type = channel_type
        self.__interaction_count = 0
        self.__interactions = []

    def analyzeIntent(self, message):
        print(f"Analysing intent for message: {message}")

    def recordInteraction(self, message):
        self.__interactions.append(message)
        self.__interaction_count += 1

    def transferToHuman(self):
        print(f"Session {self.__session_id} transferred to human support.")

    def endSession(self):
        self.__end_time = datetime.now()
        print(f"Session {self.__session_id} ended.")

    def isTimedOut(self):
        if not self.__interactions:
            return False
        last_interaction = self.__start_time if not self.__end_time else self.__end_time
        return datetime.now() - last_interaction > timedelta(minutes=30)

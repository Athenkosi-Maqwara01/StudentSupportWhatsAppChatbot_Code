from datetime import datetime

class DistressAlert:
    def __init__(self, alert_id, severity, trigger_phrases):
        self.__alert_id = alert_id
        self.__detection_time = datetime.now()
        self.__severity = severity
        self.__trigger_phrases = trigger_phrases
        self.__status = "Pending"
        self.__response_time = None
        self.__intervention_logged = False
        self.__follow_up_scheduled = False

        if self.__severity == "High":
            self.escalate_to_emergency()

    def notify_counselor(self):
        self.__response_time = datetime.now()
        self.__status = "Counselor Notified"
        # Notify logic placeholder (e.g., send email)

    def escalate_to_emergency(self):
        self.__status = "Emergency Escalated"
        self.__response_time = datetime.now()
        # Emergency protocol logic placeholder

    def log_intervention(self, outcome_details):
        self.__intervention_logged = True
        self.__status = f"Intervention Logged: {outcome_details}"

    def schedule_follow_up(self):
        if self.__severity in ["High", "Medium"]:
            self.__follow_up_scheduled = True
            self.__status = "Follow-up Scheduled"

    # Getters
    def get_alert_status(self):
        return self.__status

    def get_alert_id(self):
        return self.__alert_id

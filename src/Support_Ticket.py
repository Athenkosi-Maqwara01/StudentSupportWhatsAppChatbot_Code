from datetime import datetime, timedelta

class SupportTicket:
    SLA_PRIORITIES = {
        "high": timedelta(hours=4),
        "medium": timedelta(hours=24),
        "low": timedelta(hours=48)
    }

    def __init__(self, ticket_id, subject, description, priority, category):
        self.__ticket_id = ticket_id
        self.__subject = subject
        self.__description = description
        self.__creation_date = datetime.now()
        self.__status = "Open"
        self.__priority = priority
        self.__category = category
        self.__sla_deadline = self.__creation_date + self.SLA_PRIORITIES.get(priority.lower(), timedelta(hours=24))
        self.__agent_assigned = None
        self.__closed_date = None

    def assign_to_agent(self, agent_name):
        self.__agent_assigned = agent_name

    def update_status(self, new_status):
        self.__status = new_status
        if new_status == "Closed":
            self.__closed_date = datetime.now()

    def escalate(self):
        self.__status = "Escalated"

    def resolve_ticket(self, student_confirmation):
        if student_confirmation:
            self.update_status("Closed")

    def check_sla_violation(self):
        if datetime.now() > self.__sla_deadline and self.__status != "Closed":
            self.escalate()

    def reopen_ticket(self):
        if self.__closed_date and (datetime.now() - self.__closed_date).days <= 7:
            self.__status = "Reopened"

    # Getters for access
    def get_status(self):
        return self.__status

    def get_ticket_id(self):
        return self.__ticket_id

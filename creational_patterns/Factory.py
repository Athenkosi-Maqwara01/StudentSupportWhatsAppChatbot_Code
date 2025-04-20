from src.Support_Ticket import SupportTicket
class SupportTicketFactory:
    def create_ticket(self, ticket_type, *args, **kwargs):
        if ticket_type == "Standard":
            return SupportTicket(*args, **kwargs)
        elif ticket_type == "Urgent":
            return SupportTicket(*args, **kwargs)
        else:
            raise ValueError("Invalid ticket type")

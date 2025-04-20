from datetime import datetime, timedelta
from enum import Enum

class NotificationStatus(Enum):
    CREATED = "created"
    SENT = "sent"
    READ = "read"
    EXPIRED = "expired"

class Notification:
    def __init__(self, notification_id, content, priority, expiry_days=1):
        self.__notification_id = notification_id
        self.__content = content
        self.__timestamp = datetime.now()
        self.__status = NotificationStatus.CREATED
        self.__priority = priority
        self.__expiry_date = self.__timestamp + timedelta(days=expiry_days)

    def send(self):
        if datetime.now() < self.__expiry_date:
            self.__status = NotificationStatus.SENT
            print(f"Notification {self.__notification_id} sent.")
        else:
            self.__status = NotificationStatus.EXPIRED

    def reschedule(self, extra_days):
        self.__expiry_date += timedelta(days=extra_days)
        print(f"Notification {self.__notification_id} rescheduled.")

    def cancel(self):
        self.__status = NotificationStatus.EXPIRED

    def trackReadStatus(self):
        return self.__status

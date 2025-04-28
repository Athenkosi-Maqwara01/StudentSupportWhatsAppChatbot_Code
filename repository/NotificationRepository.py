# /repositories/NotificationRepository.py

from .Repository import Repository
from typing import Optional, List
from Notification import Notification

class NotificationRepository(Repository[Notification, int]):
    pass

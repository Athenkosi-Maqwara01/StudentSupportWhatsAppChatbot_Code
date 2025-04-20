from abc import ABC, abstractmethod
from datetime import datetime, timedelta

class User(ABC):
    def __init__(self, userId, name, phoneNumber, email, institutionId):
        self.__userId = userId
        self.__name = name
        self.__phoneNumber = phoneNumber
        self.__email = email
        self.__institutionId = institutionId
        self.__status = 'UNREGISTERED'
        self.__lastActive = datetime.now()

    @property
    def userId(self):
        return self.__userId
    
    @property
    def name(self):
        return self.__name
    
    @property
    def phoneNumber(self):
        return self.__phoneNumber
    
    @property
    def email(self):
        return self.__email
    
    @property
    def institutionId(self):
        return self.__institutionId
    
    @property
    def status(self):
        return self.__status
    
    @property
    def lastActive(self):
        return self.__lastActive

    def registerAccount(self):
        self.__status = 'ACTIVE'
        self.__lastActive = datetime.now()

    def updateProfile(self, name=None, phoneNumber=None, email=None):
        if name:
            self.__name = name
        if phoneNumber:
            self.__phoneNumber = phoneNumber
        if email:
            self.__email = email

    def deactivateAccount(self):
        self.__status = 'DEACTIVATED'

    def sendQuery(self, query):
        pass

    def checkStatus(self):
        return self.__status

    def checkAccountStatus(self):
        if self.__status == 'UNREGISTERED' and (datetime.now() - self.__lastActive).days > 30:
            self.__status = 'DORMANT'

    def optOut(self):
        self.__status = 'BLACKLISTED'


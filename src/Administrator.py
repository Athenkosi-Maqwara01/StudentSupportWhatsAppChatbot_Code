from User import User 

class Administrator(User):
    def __init__(self, userId, name, phoneNumber, email, institutionId, adminLevel, department):
        super().__init__(userId, name, phoneNumber, email, institutionId)
        self.__adminLevel = adminLevel
        self.__department = department

    @property
    def adminLevel(self):
        return self.__adminLevel
    
    @property
    def department(self):
        return self.__department
    
    def createAnnouncement(self, message):
        pass

    def broadcastMessage(self, message):
        pass

    def generateReport(self):
        pass

    def manageUsers(self):
        pass

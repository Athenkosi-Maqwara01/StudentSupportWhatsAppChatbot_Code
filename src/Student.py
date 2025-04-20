from User import User
class Student(User):
    def __init__(self, userId, name, phoneNumber, email, institutionId, studentNumber, programCode, yearOfStudy, feesBalance):
        super().__init__(userId, name, phoneNumber, email, institutionId)
        self.__studentNumber = studentNumber
        self.__programCode = programCode
        self.__yearOfStudy = yearOfStudy
        self.__feesBalance = feesBalance

    @property
    def studentNumber(self):
        return self.__studentNumber
    
    @property
    def programCode(self):
        return self.__programCode
    
    @property
    def yearOfStudy(self):
        return self.__yearOfStudy
    
    @property
    def feesBalance(self):
        return self.__feesBalance
    
    def checkSchedule(self):
        pass
    
    def viewMaterials(self):
        pass
    
    def checkFeeStatus(self):
        return self.__feesBalance
    
    def createSupportTicket(self):
        pass

from User import User

class CounselingStaff(User):
    
    def __init__(self, userId, name, phoneNumber, email, institutionId, certificationLevel, specialization):
        super().__init__(userId, name, phoneNumber, email, institutionId)
        self.__certificationLevel = certificationLevel
        self.__specialization = specialization

    @property
    def certificationLevel(self):
        return self.__certificationLevel
    
    @property
    def specialization(self):
        return self.__specialization

    def respondToDistressAlert(self, alert):
        pass

    def scheduleFollowUp(self, alert):
        pass

    def recordInterventionNotes(self, alert, notes):
        pass

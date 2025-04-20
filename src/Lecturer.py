from User import User
class Lecturer(User):
    def __init__(self, userId, name, phoneNumber, email, institutionId, staffId, department, courses):
        super().__init__(userId, name, phoneNumber, email, institutionId)
        self.__staffId = staffId
        self.__department = department
        self.__courses = courses

    @property
    def staffId(self):
        return self.__staffId
    
    @property
    def department(self):
        return self.__department
    
    @property
    def courses(self):
        return self.__courses
    
    def uploadMaterial(self, course, material):
        pass

    def sendCourseAnnouncement(self, course, message):
        pass

    def viewCourseStatistics(self, course):
        pass

import datetime

class AcademicDatabase:
    def __init__(self, connection_string: str):
        self._connection_string = connection_string
        self._last_sync_time = datetime.datetime.now()

    @property
    def last_sync_time(self):
        return self._last_sync_time

    def get_student_schedule(self, student_id: str) -> list:
        return ["AI Lecture - Monday", "Maths - Wednesday"]

    def get_course_materials(self, course_code: str) -> list:
        return ["slides.pdf", "reading.docx"]

    def get_registration_deadlines(self) -> str:
        return "30 April 2025"

    def get_payment_information(self, student_id: str) -> dict:
        return {"status": "Paid", "amount": 12000}

    def sync_data(self):
        self._last_sync_time = datetime.datetime.now()

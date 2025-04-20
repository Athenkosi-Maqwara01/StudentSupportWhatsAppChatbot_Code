from datetime import datetime

class CourseMaterial:
    def __init__(self, material_id, title, description, course_code, version, upload_date, file_type, file_size):
        self.__material_id = material_id
        self.__title = title
        self.__description = description
        self.__course_code = course_code
        self.__version = version
        self.__upload_date = upload_date
        self.__status = "Pending Approval"  # Default status
        self.__file_type = file_type
        self.__file_size = file_size
        self.__history = []  # version history for tracking changes

    # Getters and Setters
    def get_status(self):
        return self.__status

    def set_status(self, new_status):
        if new_status in ["Published", "Unpublished", "Archived", "Pending Approval"]:
            self.__status = new_status

    # Methods
    def publish(self):
        if self.__status == "Pending Approval":
            self.__status = "Published"
            print(f"Material {self.__title} has been published.")

    def unpublish(self):
        if self.__status == "Published":
            self.__status = "Unpublished"
            print(f"Material {self.__title} has been unpublished due to issues.")

    def update(self, new_title=None, new_description=None, new_version=None):
        self.__history.append((self.__title, self.__description, self.__version))
        if new_title:
            self.__title = new_title
        if new_description:
            self.__description = new_description
        if new_version:
            self.__version = new_version
        print(f"Material updated to version {self.__version}")

    def archive(self):
        self.__status = "Archived"
        print(f"Material {self.__title} has been archived.")

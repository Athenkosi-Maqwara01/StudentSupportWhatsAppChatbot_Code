from src.Course_Material import CourseMaterial 

class CourseMaterialBuilder:
    def __init__(self):
        self.material = CourseMaterial(
            material_id=None,
            title=None,
            description=None,
            course_code=None,
            version=None,
            upload_date=None,
            file_type=None,
            file_size=None
        )

    def set_title(self, title):
        self.material._CourseMaterial__title = title
        return self

    def set_description(self, description):
        self.material._CourseMaterial__description = description
        return self

    def set_course_code(self, course_code):
        self.material._CourseMaterial__course_code = course_code
        return self

    def set_version(self, version):
        self.material._CourseMaterial__version = version
        return self

    def set_upload_date(self, upload_date):
        self.material._CourseMaterial__upload_date = upload_date
        return self

    def set_file_type(self, file_type):
        self.material._CourseMaterial__file_type = file_type
        return self

    def set_file_size(self, file_size):
        self.material._CourseMaterial__file_size = file_size
        return self

    def build(self):
        return self.material

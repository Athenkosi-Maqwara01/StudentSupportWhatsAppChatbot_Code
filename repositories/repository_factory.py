from repositories.Inmemory import InMemoryCourseMaterialRepository

class RepositoryFactory:
    @staticmethod
    def get_course_material_repository():
        return InMemoryCourseMaterialRepository()

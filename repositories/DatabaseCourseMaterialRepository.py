# /repositories/database/course_material_database_repo.py

from src.Course_Material import CourseMaterial
from typing import Optional, List
from src.Course_Material import CourseMaterial

class DatabaseCourseMaterialRepository(CourseMaterial):
    def save(self, entity: CourseMaterial):
        # TODO: Implement database insert/update logic
        pass

    def find_by_id(self, entity_id: str) -> Optional[CourseMaterial]:
        # TODO: Implement database query logic
        return None

    def find_all(self) -> List[CourseMaterial]:
        # TODO: Implement logic to return all records
        return []

    def delete(self, entity_id: str):
        # TODO: Implement delete query
        pass

from typing import TypeVar, Generic, Dict, Optional, List
from abc import ABC, abstractmethod

T = TypeVar('T')
ID = TypeVar('ID')

# Repository interface
type Repository[T, ID] = 'Repository[T, ID]'

class Repository(ABC, Generic[T, ID]):
    @abstractmethod
    def save(self, entity: T) -> None:
        pass

    @abstractmethod
    def find_by_id(self, id: ID) -> Optional[T]:
        pass

    @abstractmethod
    def find_all(self) -> List[T]:
        pass

    @abstractmethod
    def delete(self, id: ID) -> None:
        pass

# Example Entity: CourseMaterial
class CourseMaterial:
    def __init__(self, material_id, title):
        self.material_id = material_id
        self.title = title

    def __repr__(self):
        return f"CourseMaterial({self.material_id}, {self.title})"

# Concrete repository for CourseMaterial
class InMemoryCourseMaterialRepository(Repository[CourseMaterial, str]):
    def __init__(self):
        self._storage: Dict[str, CourseMaterial] = {}

    def save(self, entity: CourseMaterial) -> None:
        self._storage[entity.material_id] = entity

    def find_by_id(self, id: str) -> Optional[CourseMaterial]:
        return self._storage.get(id)

    def find_all(self) -> List[CourseMaterial]:
        return list(self._storage.values())

    def delete(self, id: str) -> None:
        if id in self._storage:
            del self._storage[id]

# Unit Tests
if __name__ == '__main__':
    repo = InMemoryCourseMaterialRepository()

    mat1 = CourseMaterial("MAT001", "Intro to AI")
    mat2 = CourseMaterial("MAT002", "Data Science")

    # Test Save
    repo.save(mat1)
    repo.save(mat2)

    # Test Find by ID
    assert repo.find_by_id("MAT001") == mat1

    # Test Find All
    all_materials = repo.find_all()
    assert len(all_materials) == 2

    # Test Delete
    repo.delete("MAT001")
    assert repo.find_by_id("MAT001") is None
    assert len(repo.find_all()) == 1

    print("All tests passed.")

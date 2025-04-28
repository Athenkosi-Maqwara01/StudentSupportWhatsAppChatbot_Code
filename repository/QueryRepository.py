# /repositories/QueryRepository.py

from .Repository import Repository
from typing import Optional, List
from Query import Query

class QueryRepository(Repository[Query, int]):
    pass

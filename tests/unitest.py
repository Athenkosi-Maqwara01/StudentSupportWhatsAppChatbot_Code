from creational_patterns.Abstract import SupportSystemFactory, StudentSupportFactory
from creational_patterns.Simple import ObjectFactory
from creational_patterns.Factory import SupportTicketFactory
from creational_patterns.Builder import CourseMaterialBuilder
from creational_patterns.Prototype import  QueryPrototype
from creational_patterns.Singleton import Database
from src.Query import Query 
from src.Support_Ticket import SupportTicket
from src.Response import Response


import unittest

class TestCreationalPatterns(unittest.TestCase):
    
    def test_simple_factory(self):
        query = ObjectFactory.create_object('Query', 1, "Help", "Academic", 0.9)
        self.assertIsInstance(query, Query)

    def test_factory_method(self):
        factory = SupportTicketFactory()
        ticket = factory.create_ticket("Standard", 1, "Issue", "Description", "Medium", "Tech Support")
        self.assertIsInstance(ticket, SupportTicket)

    def test_abstract_factory(self):
        factory = StudentSupportFactory()
        query = factory.create_query()
        response = factory.create_response()
        self.assertIsInstance(query, Query)
        self.assertIsInstance(response,Response )

    def test_builder_pattern(self):
        builder = CourseMaterialBuilder()
        material = builder.set_title("Data Science").set_course_code("CS101").build()
        self.assertEqual(material._CourseMaterial__title, "Data Science")
        self.assertEqual(material._CourseMaterial__course_code, "CS101")

    def test_prototype_pattern(self):
        original_query = Query(1, "Help with course material", "Academic", 0.8)
        prototype = QueryPrototype(original_query)
        cloned_query = prototype.clone()
        self.assertNotEqual(id(original_query), id(cloned_query.query))

    def test_singleton_pattern(self):
        db1 = Database("ConnectionString1")
        db2 = Database("ConnectionString2")
        self.assertIs(db1, db2)  # Same instance

if __name__ == '__main__':
    unittest.main()

import unittest
from models.city import City
from models.country import Country

class TestCity(unittest.TestCase):
    
    def setUp(self):
        self.city = City("Beijing", "China", "Tiananmen Square")
    
    
    def test_city_has_name(self):
        self.assertEqual("Beijing", self.city.name)
        
        
    def test_city_has_sight(self):
        self.assertEqual("Tiananmen Square", self.city.sight)

    def test_city_has_country(self):
        self.assertEqual("China", self.city.country )
       
        
    def test_visited_starts_false(self):
        self.assertEqual(False, self.city.visited)
        
    
    def test_can_set_as_visited(self):
        self.city.set_as_visited()
        self.assertEqual(True, self.city.visited)

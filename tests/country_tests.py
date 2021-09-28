import unittest
from models.country import Country

class TestCountry(unittest.TestCase):
    
    def setUp(self):
        self.country = Country("China")
        
    
    
    def test_country_has_name(self):
        self.assertEqual("China", self.country.name)

  
        
        
   

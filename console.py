import pdb 
from models.city import City
import repositories.city_repository as city_repository 
from models.country import Country
import repositories.country_repository as country_repository 

city_repository.delete_all()
country_repository.delete_all()

country1 = Country("China")
country_repository.save(country1)

country2 = Country("France")
country_repository.save(country2)

country3 = Country("Italy")
country_repository.save(country3)

city1 = City("Beijing", "Tiananmen Square", country1)
city_repository.save(city1)

city2 = City("Paris", "Eiffel Tower", country2)
city_repository.save(city2)

city3 = City("Rome", "Colosseum", country3)
city_repository.save(city3)

city4 = City("Venice", "Grand Canal", country3)
city_repository.save(city4)



pdb.set_trace()







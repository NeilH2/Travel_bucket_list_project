from db.run_sql import run_sql

from models.city import City
import repositories.country_repository as country_repository
  
def select_all():  
    cities = [] 

    sql = "SELECT * FROM cities"
    results = run_sql(sql)

    for item in results:
        country = country_repository.select(item['country_id'])
        city = City(item['name'], item['sight'], country ,item['visited'], item['id'] )
        cities.append(city)
    return cities 

def save(city):
        sql = "INSERT INTO cities (name,  sight, country_id, visited) VALUES (%s,%s,%s,%s) RETURNING *"
        values = [city.name, city.sight, city.country.id, city.visited]
        results = run_sql(sql, values)
        id = results[0]['id']
        city.id = id
        return city

def select(id):
    city = None
    sql = "SELECT * FROM cities WHERE id= %s" 
    values=[id]  
    result = run_sql(sql, values)[0]

    if result is not None:
        country = country_repository.select(result['country_id'])
        city = City(result['name'],  result['sight'], country, result['visited'], result['id'])  
        return city


def delete_all():
    sql = "DELETE FROM cities"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM cities WHERE id = %s" 
    values = [id]   
    run_sql(sql, values)

def update(city):
    sql = "UPDATE cities SET (name,  sight, country_id, visited) = (%s, %s, %s, %s) where id = %s" 
    values = [city.name, city.sight, city.country.id, city.visited, city.id]
    run_sql(sql, values)
from flask import Blueprint, render_template, request, redirect
from models.city import City
from models.country import Country
import repositories.city_repository as city_repository
import repositories.country_repository as country_repository
import pdb



destinations_cities_blueprint = Blueprint("cities", __name__)

@destinations_cities_blueprint.route("/cities")
def city_destinations():
    cities = city_repository.select_all()
    return render_template("/cities/index.html" , all_cities = cities)

@destinations_cities_blueprint.route("/cities/new", methods=['GET']) 
def new_city():
    cities = city_repository.select_all()
    countries = country_repository.select_all()
    return render_template("cities/new.html", all_cities = cities, all_countries = countries)

@destinations_cities_blueprint.route("/cities", methods=['POST'])
def create_new_city():

    name = request.form['name']
    sight = request.form['sight']
    country_id = request.form['country_id']
    visited = request.form['visited']
    country = country_repository.select(country_id)
    city = City(name, sight, country, visited)
    city_repository.save(city)
    return redirect('/cities')

@destinations_cities_blueprint.route("/cities/<id>/delete", methods=['POST'])
def delete_city(id):
    city_repository.delete(id)
    return redirect('/cities') 

@destinations_cities_blueprint.route("/cities/<id>", methods=['GET'])
def show_city(id):
    city = city_repository.select(id)
    return render_template('cities/show.html', city = city)

@destinations_cities_blueprint.route("/cities/<id>/edit", methods=['GET'])
def edit_city(id):
    city = city_repository.select(id)
    countries = country_repository.select_all()
    return render_template('cities/edit.html', city = city, all_countries = countries)

@destinations_cities_blueprint.route("/cities/<id>", methods=['POST'])
def update_city(id):
    name = request.form['name']
    sight = request.form['sight']
    country_id = request.form['country_id']
    visited = request.form['visited']
    country = country_repository.select(country_id)
    city = City(name, sight, country, visited, id)
    city_repository.update(city)
    return redirect('/cities') 

@destinations_cities_blueprint.route("/cities/visited")
def cities_visited():
    cities = city_repository.select_all()
    return render_template("cities/visited.html", cities = cities)

@destinations_cities_blueprint.route("/cities/tovisit")
def cities_to_visit():
    cities = city_repository.select_all()
    return render_template("cities/tovisit.html", cities = cities)



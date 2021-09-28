from flask import Blueprint, render_template, request, redirect
from models.country import Country
import repositories.country_repository as country_repository



destinations_countries_blueprint = Blueprint("countries", __name__)

@destinations_countries_blueprint.route("/countries")
def country_destinations():
    countries = country_repository.select_all()
    return render_template("/countries/index.html" , all_countries = countries)

@destinations_countries_blueprint.route("/countries/new", methods=['GET']) 
def new_country():
    countries = country_repository.select_all()
    return render_template("countries/new.html", all_countries = countries) 

@destinations_countries_blueprint.route("/countries", methods=['POST'])
def create_new_country():

    name = request.form['name']
    country = Country(name)
    country_repository.save(country)
    return redirect('/countries')  

@destinations_countries_blueprint.route("/countries/<id>/delete", methods=['POST'])
def delete_country(id):
    country_repository.delete(id)
    return redirect('/countries')   

@destinations_countries_blueprint.route("/countries/<id>", methods=['GET'])
def show_country(id):
    country = country_repository.select(id)
    return render_template('countries/show.html', country = country) 

@destinations_countries_blueprint.route("/countries/<id>/edit", methods=['GET'])
def edit_country(id):
    country = country_repository.select(id)
    return render_template('countries/edit.html', country = country)            




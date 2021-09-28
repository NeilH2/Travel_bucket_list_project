from flask import Flask, render_template
from controllers.city_controller import destinations_cities_blueprint
from controllers.country_controller import destinations_countries_blueprint


app = Flask(__name__)

app.register_blueprint(destinations_cities_blueprint)
app.register_blueprint(destinations_countries_blueprint)




@app.route('/home')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
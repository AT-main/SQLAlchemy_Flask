"""
    This flask application reads data of Canada cities from 
    a database on the disk, in the same directory where application 
    is located, and provides this data through endpoints to the user
    through a html page with two select elements.
"""
from flask import Flask, render_template, jsonify, request
from models import *  # import Province and City classes

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///ca.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)


@app.route("/")
def index():
    """
        When the home page is loaded, the list of provinces
        are also loaded to the first select element of the
        page.
    """
    provinces = Province.query.all()
    return render_template("index.html", provinces=provinces)


@app.route("/province", methods=['POST'])
def cities():
    """
        This function return the list of cities of the given 
        province specified by corresponding province_id.
    """
    try:
        province_id = int(request.form.get("province_id"))
    except:
        return jsonify({'Error': 'id should be of type Integer'})
        
    cities = Province.query.get(province_id).cities
    if cities is None:
        return render_template("error.html", message="No such province.")

    # create a list capable to be converted to a json object using jsonify
    list_cities = []
    for city in cities:
        list_cities.append({'id': city.id, 'name': city.name})

    # This one also works: return jsonify({'cities': list_cities})
    return jsonify(cities=list_cities)


@app.route("/city/<int:city_id>", methods=['POST'])
def single_city(city_id):
    """
        receiving the id of a city and returning the population
        of that city.
    """
    city = City.query.get(city_id)
    if city is None:
        return jsonify({'Error': 'No such city!'})

    return jsonify(population=city.population, extra=2)


if __name__ == "__main__":
    app.run(debug=True)

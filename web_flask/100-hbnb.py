#!/usr/bin/pyhton3
"""Starting a flask web app"""
from flask import Flask, jsonify, request, make_response
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exception):
    """Closes the database at the end of the request."""
    storage.close()


@app.route('/states/<state_id>/cities', methods=['GET'])
def get_cities_by_state(state_id):
    """Get all cities of a given state."""
    state = storage.get("State", state_id)
    if not state:
        return jsonify({'error': 'State not found'}), 404

    cities = [city.to_dict() for city in state.cities]
    return jsonify(cities)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

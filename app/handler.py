from flask import make_response, jsonify
from app import app


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not Found'}), 404)


@app.errorhandler(500)
def internal_error(error):
    return make_response(jsonify({'error': 'Internal Server Error'}), 500)
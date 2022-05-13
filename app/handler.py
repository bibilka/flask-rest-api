from flask import make_response, jsonify
from app import app


# обработка 404 ошибки (не найдено)
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not Found'}), 404)


# обработка 500 ошибки (остальные внутренние ошибки в приложении)
@app.errorhandler(500)
def internal_error(error):
    return make_response(jsonify({'error': 'Internal Server Error'}), 500)

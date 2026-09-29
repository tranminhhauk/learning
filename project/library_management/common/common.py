from flask import jsonify

def format_resp(msg:dict, status_code: int):
    return jsonify(msg), status_code

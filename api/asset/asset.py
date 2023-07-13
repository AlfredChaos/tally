import json
from api.asset import asset_bp
from cache import log
from flask import request, jsonify, make_response

Log = log.get_global_log()

@asset_bp.route("/create/", methods=["POST"])
def create():
    params = request.get_json()
    Log.info(f"===Get Params = {params}")
    return make_response("", 200)

@asset_bp.route("/update", methods=["PUT"])
def update():
    pass

@asset_bp.route("/create", methods=["DELETE"])
def delete():
    pass

@asset_bp.route("/create", methods=["GET"])
def get():
    pass

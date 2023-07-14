import json
from cache import log
from flask import Blueprint, request, jsonify, make_response

Log = log.get_global_log()
asset_bp = Blueprint('asset', __name__)

@asset_bp.route("/create/", methods=["POST"])
def create():
    params = request.get_json()
    Log.info(f"===Get Params = {params}")
    return make_response("", 200)

@asset_bp.route("/update", methods=["PUT"])
def update():
    pass

@asset_bp.route("/delete", methods=["DELETE"])
def delete():
    pass

@asset_bp.route("/get/", methods=["GET"])
def get():
    pass

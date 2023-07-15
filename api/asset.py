from api.base import db_mix
from cache import log
from common import exception
from flask import Blueprint, request, jsonify

LOG = log.get_global_log()
asset_bp = Blueprint('asset', __name__)


@asset_bp.route("/create", methods=["POST"])
def create():
    params = request.get_json()
    user_uuid = params.get('user_uuid', '')
    if not user_uuid:
        raise exception.InvalidParamsException(
            f'user_uuid is required, params = {params}')
    body = {
        'user_uuid': user_uuid,
        'fixed': params.get('fixed', 0),
        'debt': params.get('debt', 0),
        'cash': params.get('cash', 0),
        'finance': params.get('finance', 0)
    }
    db_mix.create_asset(body)
    return jsonify(params)


@asset_bp.route("/update", methods=["PUT"])
def update():
    pass


@asset_bp.route("/delete", methods=["DELETE"])
def delete():
    pass


@asset_bp.route("/get", methods=["GET"])
def get():
    pass

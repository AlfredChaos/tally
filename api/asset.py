from api.base import db_mix
from cache import log
from common import exception
from flask import Blueprint, request, jsonify, make_response

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
    asset = db_mix.create_asset(body)
    return jsonify(asset)


@asset_bp.route("/update", methods=["PUT"])
def update():
    id = request.args.get('id')
    params = request.get_json()
    try:
        asset = db_mix.update_asset(id, params)
    except Exception as e:
        return make_response(f"update failed: {e}", 500)
    return jsonify(asset)


@asset_bp.route("/delete", methods=["DELETE"])
def delete():
    id = request.args.get('id')
    try:
        db_mix.delete_asset(id)
    except Exception as e:
        return make_response(f"delete failed: {e}", 500)
    return make_response("delete succed", 200)


@asset_bp.route("/get", methods=["GET"])
def get():
    id = request.args.get('id')
    asset = db_mix.get_asset(id)
    return jsonify(asset)


@asset_bp.route("/list", methods=["GET"])
def list():
    filters = {}
    user_uuid = request.args.get('user_uuid')
    if user_uuid:
        filters['user_uuid'] = user_uuid
    assets = db_mix.list_assets(filters)
    return jsonify(assets)

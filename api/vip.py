from api.base import db_mix
from cache import log
from common import exception
from flask import Blueprint, request, jsonify, make_response

LOG = log.get_global_log()
vip_bp = Blueprint('vip', __name__)


@vip_bp.route("/create", methods=["POST"])
def create():
    params = request.get_json()
    user_uuid = params.get('user_uuid', '')
    if not user_uuid:
        raise exception.InvalidParamsException(
            f'user_uuid is required, params = {params}')
    body = {
        'user_uuid': user_uuid,
        'name': params.get('name', ''),
        'fee': params.get('fee', 0),
        'deduct_date': params.get('deduct_date', ''),
        'deduct_period': params.get('deduct_period', ''),
        'payment_channel': params.get('payment_channel', '')
    }
    vip = db_mix.create_vip(body)
    return jsonify(vip)


@vip_bp.route("/update", methods=["PUT"])
def update():
    id = request.args.get('id')
    params = request.get_json()
    try:
        vip = db_mix.update_vip(id, params)
    except Exception as e:
        return make_response(f"update failed: {e}", 500)
    return jsonify(vip)


@vip_bp.route("/delete", methods=["DELETE"])
def delete():
    id = request.args.get('id')
    try:
        db_mix.delete_vip(id)
    except Exception as e:
        return make_response(f"delete failed: {e}", 500)
    return make_response("delete succed", 200)


@vip_bp.route("/get", methods=["GET"])
def get():
    id = request.args.get('id')
    vip = db_mix.get_vip(id)
    return jsonify(vip)


@vip_bp.route("/list", methods=["GET"])
def list():
    filters = {}
    user_uuid = request.args.get('user_uuid')
    if user_uuid:
        filters['user_uuid'] = user_uuid
    vips = db_mix.list_vips(filters)
    return jsonify(vips)

from api.base import db_mix
from cache import log
from common import exception
from flask import Blueprint, request, jsonify, make_response

LOG = log.get_global_log()
card_bp = Blueprint('card', __name__)


@card_bp.route("/create", methods=["POST"])
def create():
    params = request.get_json()
    user_uuid = params.get('user_uuid', '')
    if not user_uuid:
        raise exception.InvalidParamsException(
            f'user_uuid is required, params = {params}')
    body = {
        'user_uuid': user_uuid,
        'name': params.get('name', ''),
        'bank': params.get('bank', ''),
        'card_type': params.get('card_type', ''),
        'deposit': params.get('deposit', 0)
    }
    card = db_mix.create_card(body)
    return jsonify(card)


@card_bp.route("/update", methods=["PUT"])
def update():
    id = request.args.get('id')
    params = request.get_json()
    try:
        card = db_mix.update_card(id, params)
    except Exception as e:
        return make_response(f"update failed: {e}", 500)
    return jsonify(card)


@card_bp.route("/delete", methods=["DELETE"])
def delete():
    id = request.args.get('id')
    try:
        db_mix.delete_card(id)
    except Exception as e:
        return make_response(f"delete failed: {e}", 500)
    return make_response("delete succed", 200)


@card_bp.route("/get", methods=["GET"])
def get():
    id = request.args.get('id')
    card = db_mix.get_card(id)
    return jsonify(card)

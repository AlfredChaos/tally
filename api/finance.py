from api.base import db_mix
from cache import log
from common import exception
from flask import Blueprint, request, jsonify, make_response

LOG = log.get_global_log()
finance_bp = Blueprint('finance', __name__)


@finance_bp.route("/create", methods=["POST"])
def create():
    params = request.get_json()
    user_uuid = params.get('user_uuid', '')
    if not user_uuid:
        raise exception.InvalidParamsException(
            f'user_uuid is required, params = {params}')
    body = {
        'user_uuid': user_uuid,
        'fund': params.get('fund', 0),
        'insurance': params.get('insurance', 0),
        'stock': params.get('stock', 0),
        'bank': params.get('bank', 0)
    }
    finance = db_mix.create_finance(body)
    return jsonify(finance)


@finance_bp.route("/update", methods=["PUT"])
def update():
    id = request.args.get('id')
    params = request.get_json()
    try:
        finance = db_mix.update_finance(id, params)
    except Exception as e:
        return make_response(f"update failed: {e}", 500)
    return jsonify(finance)


@finance_bp.route("/delete", methods=["DELETE"])
def delete():
    id = request.args.get('id')
    try:
        db_mix.delete_finance(id)
    except Exception as e:
        return make_response(f"delete failed: {e}", 500)
    return make_response("delete succed", 200)


@finance_bp.route("/get", methods=["GET"])
def get():
    id = request.args.get('id')
    finance = db_mix.get_finance(id)
    return jsonify(finance)

from api.base import db_mix
from cache import log
from common import exception
from flask import Blueprint, request, jsonify, make_response

LOG = log.get_global_log()
income_bp = Blueprint('income', __name__)


@income_bp.route("/create", methods=["POST"])
def create():
    params = request.get_json()
    user_uuid = params.get('user_uuid', '')
    if not user_uuid:
        raise exception.InvalidParamsException(
            f'user_uuid is required, params = {params}')
    body = {
        'user_uuid': user_uuid,
        'name': params.get('name', ''),
        'tag_id': params.get('tag_id', ''),
        'income': params.get('income', 0)
    }
    income = db_mix.create_income(body)
    return jsonify(income)


@income_bp.route("/update", methods=["PUT"])
def update():
    id = request.args.get('id')
    params = request.get_json()
    try:
        income = db_mix.update_income(id, params)
    except Exception as e:
        return make_response(f"update failed: {e}", 500)
    return jsonify(income)


@income_bp.route("/delete", methods=["DELETE"])
def delete():
    id = request.args.get('id')
    try:
        db_mix.delete_income(id)
    except Exception as e:
        return make_response(f"delete failed: {e}", 500)
    return make_response("delete succed", 200)


@income_bp.route("/get", methods=["GET"])
def get():
    id = request.args.get('id')
    income = db_mix.get_income(id)
    return jsonify(income)


@income_bp.route("/list", methods=["GET"])
def list():
    filters = {}
    tag_id = request.args.get('tag_id')
    user_uuid = request.args.get('user_uuid')
    if tag_id:
        filters['tag_id'] = tag_id
    if user_uuid:
        filters['user_uuid'] = user_uuid
    incomes = db_mix.list_incomes(filters)
    return jsonify(incomes)
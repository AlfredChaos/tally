from api.base import db_mix
from cache import log
from common import exception
from flask import Blueprint, request, jsonify, make_response
from models.budget import BudgetPeriod

LOG = log.get_global_log()
budget_bp = Blueprint('budget', __name__)


@budget_bp.route("/create", methods=["POST"])
def create():
    params = request.get_json()
    user_uuid = params.get('user_uuid', '')
    if not user_uuid:
        raise exception.InvalidParamsException(
            f'user_uuid is required, params = {params}')
    body = {
        'user_uuid': user_uuid,
        'period': params.get('period', BudgetPeriod.DAY),
        'money': params.get('money', 0)
    }
    budget = db_mix.create_budget(body)
    return jsonify(budget)


@budget_bp.route("/update", methods=["PUT"])
def update():
    id = request.args.get('id')
    params = request.get_json()
    try:
        budget = db_mix.update_budget(id, params)
    except Exception as e:
        return make_response(f"update failed: {e}", 500)
    return jsonify(budget)


@budget_bp.route("/delete", methods=["DELETE"])
def delete():
    id = request.args.get('id')
    try:
        db_mix.delete_budget(id)
    except Exception as e:
        return make_response(f"delete failed: {e}", 500)
    return make_response("delete succed", 200)


@budget_bp.route("/get", methods=["GET"])
def get():
    id = request.args.get('id')
    budget = db_mix.get_budget(id)
    return jsonify(budget)

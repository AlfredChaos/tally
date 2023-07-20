from api.base import db_mix
from cache import log
from common import exception
from flask import Blueprint, request, jsonify, make_response

LOG = log.get_global_log()
fund_bp = Blueprint('fund', __name__)


@fund_bp.route("/create", methods=["POST"])
def create():
    params = request.get_json()
    user_uuid = params.get('user_uuid', '')
    if not user_uuid:
        raise exception.InvalidParamsException(
            f'user_uuid is required, params = {params}')
    body = {
        'user_uuid': user_uuid,
        'money': params.get('money', 0),
        'fund_type': params.get('fund_type', ''),
        'description': params.get('description', ''),
        'auto_investment': params.get('auto_investment', False),
        'auto_investment_strategy': params.get('auto_investment_strategy', ''),
        'auto_investment_period': params.get('auto_investment_period', ''),
        'auto_investment_money': params.get('auto_investment_money', 0),
        'strategy_type': params.get('strategy_type', '')
    }
    fund = db_mix.create_fund(body)
    return jsonify(fund)


@fund_bp.route("/update", methods=["PUT"])
def update():
    id = request.args.get('id')
    params = request.get_json()
    try:
        fund = db_mix.update_fund(id, params)
    except Exception as e:
        return make_response(f"update failed: {e}", 500)
    return jsonify(fund)


@fund_bp.route("/delete", methods=["DELETE"])
def delete():
    id = request.args.get('id')
    try:
        db_mix.delete_fund(id)
    except Exception as e:
        return make_response(f"delete failed: {e}", 500)
    return make_response("delete succed", 200)


@fund_bp.route("/get", methods=["GET"])
def get():
    id = request.args.get('id')
    fund = db_mix.get_fund(id)
    return jsonify(fund)


@fund_bp.route("/list", methods=["GET"])
def list():
    filters = {}
    user_uuid = request.args.get('user_uuid')
    if user_uuid:
        filters['user_uuid'] = user_uuid
    funds = db_mix.list_funds(filters)
    return jsonify(funds)

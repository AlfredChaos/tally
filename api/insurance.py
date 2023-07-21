from api.base import db_mix
from cache import log
from common import exception
from flask import Blueprint, request, jsonify, make_response

LOG = log.get_global_log()
insurance_bp = Blueprint('insurance', __name__)


@insurance_bp.route("/create", methods=["POST"])
def create():
    params = request.get_json()
    user_uuid = params.get('user_uuid', '')
    start_date = params.get('start_date', '')
    end_date = params.get('end_date', '')
    if not user_uuid:
        raise exception.InvalidParamsException(
            f'user_uuid is required, params = {params}')
    if not start_date:
        raise exception.InvalidParamsException(
            f'start_at is required, params = {params}')
    if not end_date:
        raise exception.InvalidParamsException(
            f'end_date is required, params = {params}')
    body = {
        'user_uuid': user_uuid,
        'start_date': params.get('start_date'),
        'end_date': params.get('end_date'),
        'description': params.get('description', ''),
        'insurance_type': params.get('insurance_type', ''),
        'insurance_period': params.get('insurance_period', ''),
        'money_per_period': params.get('money_per_period', 0),
        'amount': params.get('amount', 0),
        'excepted_income': params.get('excepted_income', '')
    }
    insurance = db_mix.create_insurance(body)
    return jsonify(insurance)


@insurance_bp.route("/update", methods=["PUT"])
def update():
    id = request.args.get('id')
    params = request.get_json()
    try:
        insurance = db_mix.update_insurance(id, params)
    except Exception as e:
        return make_response(f"update failed: {e}", 500)
    return jsonify(insurance)


@insurance_bp.route("/delete", methods=["DELETE"])
def delete():
    id = request.args.get('id')
    try:
        db_mix.delete_insurance(id)
    except Exception as e:
        return make_response(f"delete failed: {e}", 500)
    return make_response("delete succed", 200)


@insurance_bp.route("/get", methods=["GET"])
def get():
    id = request.args.get('id')
    insurance = db_mix.get_insurance(id)
    return jsonify(insurance)


@insurance_bp.route("/list", methods=["GET"])
def list():
    filters = {}
    user_uuid = request.args.get('user_uuid')
    if user_uuid:
        filters['user_uuid'] = user_uuid
    insurances = db_mix.list_insurances(filters)
    return jsonify(insurances)

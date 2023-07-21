from api.base import db_mix
from cache import log
from common import exception
from flask import Blueprint, request, jsonify, make_response

LOG = log.get_global_log()
stock_bp = Blueprint('stock', __name__)


@stock_bp.route("/create", methods=["POST"])
def create():
    params = request.get_json()
    user_uuid = params.get('user_uuid', '')
    if not user_uuid:
        raise exception.InvalidParamsException(
            f'user_uuid is required, params = {params}')
    body = {
        'user_uuid': user_uuid,
        'name': params.get('name', ''),
        'money': params.get('money', ''),
        'description': params.get('description', '')
    }
    stock = db_mix.create_stock(body)
    return jsonify(stock)


@stock_bp.route("/update", methods=["PUT"])
def update():
    id = request.args.get('id')
    params = request.get_json()
    try:
        stock = db_mix.update_stock(id, params)
    except Exception as e:
        return make_response(f"update failed: {e}", 500)
    return jsonify(stock)


@stock_bp.route("/delete", methods=["DELETE"])
def delete():
    id = request.args.get('id')
    try:
        db_mix.delete_stock(id)
    except Exception as e:
        return make_response(f"delete failed: {e}", 500)
    return make_response("delete succed", 200)


@stock_bp.route("/get", methods=["GET"])
def get():
    id = request.args.get('id')
    stock = db_mix.get_stock(id)
    return jsonify(stock)


@stock_bp.route("/list", methods=["GET"])
def list():
    filters = {}
    user_uuid = request.args.get('user_uuid')
    if user_uuid:
        filters['user_uuid'] = user_uuid
    stocks = db_mix.list_stocks(filters)
    return jsonify(stocks)

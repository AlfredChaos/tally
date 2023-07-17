from api.base import db_mix
from cache import log
from common import exception
from flask import Blueprint, request, jsonify, make_response
from models.tag import TagType

LOG = log.get_global_log()
tag_bp = Blueprint('tag', __name__)


@tag_bp.route("/create", methods=["POST"])
def create():
    params = request.get_json()
    user_uuid = params.get('user_uuid', '')
    if not user_uuid:
        raise exception.InvalidParamsException(
            f'user_uuid is required, params = {params}')
    body = {
        'user_uuid': user_uuid,
        'name': params.get('name', ''),
        'tag_type': params.get('tag_type', TagType.EXPAND)
    }
    tag = db_mix.create_tag(body)
    return jsonify(tag)


@tag_bp.route("/update", methods=["PUT"])
def update():
    id = request.args.get('id')
    params = request.get_json()
    try:
        tag = db_mix.update_tag(id, params)
    except Exception as e:
        return make_response(f"update failed: {e}", 500)
    return jsonify(tag)


@tag_bp.route("/delete", methods=["DELETE"])
def delete():
    id = request.args.get('id')
    try:
        db_mix.delete_tag(id)
    except Exception as e:
        return make_response(f"delete failed: {e}", 500)
    return make_response("delete succed", 200)


@tag_bp.route("/get", methods=["GET"])
def get():
    id = request.args.get('id')
    tag = db_mix.get_tag(id)
    return jsonify(tag)


@tag_bp.route("/list", methods=["GET"])
def list():
    filters = {}
    name = request.args.get('name')
    user_uuid = request.args.get('user_uuid')
    if name:
        filters['name'] = name
    if user_uuid:
        filters['user_uuid'] = user_uuid
    tags = db_mix.list_tags(filters)
    return jsonify(tags)
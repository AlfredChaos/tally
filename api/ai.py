from api.base import db_mix
from cache import log
from common import exception
from flask import Blueprint, request, jsonify, make_response

LOG = log.get_global_log()
ai_bp = Blueprint('ai', __name__)


@ai_bp.route("/prompt", methods=["POST"])
def prompt():
    pass

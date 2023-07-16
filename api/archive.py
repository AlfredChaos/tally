from api.base import db_mix
from cache import log
from common import exception
from flask import Blueprint, request, jsonify, make_response

LOG = log.get_global_log()
archive_bp = Blueprint('archive', __name__)


@archive_bp.route("/archive", methods=["POST"])
def archive():
    pass

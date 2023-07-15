from apps import root
from allog.python import pylog
from allog.python.pylog import Level
from cache import config

global_log = None


def get_global_log():
    global global_log
    if not global_log:
        global_log = root.log
    return global_log

from allog.python import pylog
from allog.python.pylog import Level
from cache import config

global_log = None


def get_global_log():
    global global_log
    if not global_log:
        global_log = init_log()
    return global_log


def init_log():
    log_file = config.global_config['Log']['file']
    log_level = config.global_config['Log']['level']
    log_output = config.global_config['Log']['output']
    if log_output == 'stdout':
        log_file = None
    log_level = Level.get_level(log_level)
    return pylog.log(file=log_file, level=log_level)

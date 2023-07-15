import configparser
import os
from allog.python import pylog
from allog.python.pylog import Level
from cache import config
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


class RegisterApp(object):

    def __init__(self) -> None:
        self.app = Flask(__name__)
        self.path_file = "config.ini"
        self.config = configparser.ConfigParser()
        self.current_dir = self._get_current_path()
        self.config.read(self.current_dir + '/' + self.path_file)
        self._update_global_cache()
        self.log = self._init_log()
        self.db = self.connct_database()

    def _get_current_path(self):
        current_file = os.path.realpath(__file__)
        return os.path.dirname(current_file)
    
    def _update_global_cache(self):
        for new_key, item in self.config.items():
            if new_key == 'DEFAULT':
                new_key = 'Default'
            if new_key not in config.global_config:
                config.global_config[new_key] = item
                continue
            for k, d in item.items():
                config.global_config[new_key][k] = d

    def _init_log(self):
        log_file = config.global_config['Log']['file']
        log_level = config.global_config['Log']['level']
        log_output = config.global_config['Log']['output']
        if log_output == 'stdout':
            log_file = None
        log_level = Level.get_level(log_level)
        return pylog.log(file=log_file, level=log_level)

    def get_current_config(self):
        return config.global_config
                
    def debug_enable(self, enable):
        self.app.debug = enable
    
    def run(self):
        host = config.global_config['Default']['server']
        port = config.global_config['Default']['port']
        self.app.run(host=host, port=port)

    def connct_database(self):
        host = config.global_config['Db']['host']
        port = config.global_config['Db']['port']
        username = config.global_config['Db']['username']
        password = config.global_config['Db']['password']
        database = config.global_config['Db']['database']
        self.db_uri = 'mysql+pymysql://' + username + ':' + password + '@' + \
            host + ':' + port + '/' + database + '?charset=utf8'
        self.app.config['SQLALCHEMY_DATABASE_URI'] = self.db_uri
        self.app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
        return SQLAlchemy(self.app)
    
    def register_blueprint(self, bp, url_prefix):
        self.app.register_blueprint(bp, url_prefix)


root = RegisterApp()
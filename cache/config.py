global_config = {
    "Default": {
        "project": "tally",
        "server": "localhost",
        "port": 8080
    },
    "Db": {
        "host": "localhost",
        "port": 3306,
        "username": "root",
        "password": "root",
        "database": "tally"
    },
    "Log": {
        "file": "./tally.log",
        "level": "Debug",
        "output": "stdout"
    }
}


def get_global_config():
    return global_config

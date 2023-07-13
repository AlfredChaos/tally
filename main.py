import apps
from api.ai import ai_bp
from api.archive import archive_bp
from api.budget import budget_bp
from api.card import card_bp
from api.chart import chart_bp
from api.finance import finance_bp
from api.income import income_bp
from api.asset import asset_bp
from api.tag import tag_bp
from api.vip import vip_bp
from cache import log, database


def register_blueprint(root):
    root.app.register_blueprint(ai_bp, url_prefix='/ai/')
    root.app.register_blueprint(archive_bp, url_prefix='/archive/')
    root.app.register_blueprint(budget_bp, url_prefix='/budget/')
    root.app.register_blueprint(card_bp, url_prefix='/card/')
    root.app.register_blueprint(chart_bp, url_prefix='/chart/')
    root.app.register_blueprint(finance_bp, url_prefix='/finance/')
    root.app.register_blueprint(income_bp, url_prefix='/income/')
    root.app.register_blueprint(asset_bp, url_prefix='/asset/')
    root.app.register_blueprint(tag_bp, url_prefix='/tag/')
    root.app.register_blueprint(vip_bp, url_prefix='/vip/')


if __name__ == '__main__':
    root = apps.RegisterApp()
    register_blueprint(root)
    database.update_db_connection(root.db)
    try:
        root.run()
    except Exception as e:
        root.app.logger.error(f"tally runtime error = {e}")
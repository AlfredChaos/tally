from apps import root
from api.ai import ai_bp
from api.archive import archive_bp
from api.budget import budget_bp
from api.card import card_bp
from api.chart import chart_bp
from api.finance import finance_bp
from api.fund import fund_bp
from api.income import income_bp
from api.asset import asset_bp
from api.tag import tag_bp
from api.vip import vip_bp
from api.insurance import insurance_bp
from api.stock import stock_bp


def register_blueprint(root):
    root.app.register_blueprint(ai_bp, url_prefix='/ai/')
    root.app.register_blueprint(archive_bp, url_prefix='/archive/')
    root.app.register_blueprint(budget_bp, url_prefix='/budget/')
    root.app.register_blueprint(card_bp, url_prefix='/card/')
    root.app.register_blueprint(chart_bp, url_prefix='/chart/')
    root.app.register_blueprint(finance_bp, url_prefix='/finance/')
    root.app.register_blueprint(fund_bp, url_prefix='/fund/')
    root.app.register_blueprint(income_bp, url_prefix='/income/')
    root.app.register_blueprint(asset_bp, url_prefix='/asset/')
    root.app.register_blueprint(tag_bp, url_prefix='/tag/')
    root.app.register_blueprint(vip_bp, url_prefix='/vip/')
    root.app.register_blueprint(insurance_bp, url_prefix='/insurance/')
    root.app.register_blueprint(stock_bp, url_prefix='/stock_bp/')


if __name__ == '__main__':
    register_blueprint(root)
    try:
        root.run()
    except Exception as e:
        root.app.logger.error(f"tally runtime error = {e}")
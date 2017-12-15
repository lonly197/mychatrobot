# -*- coding: utf-8 -*-

from sanic import Sanic

from ChartRobot.settings import Config

blueprints = []


def create_app(register_bp=True, test=False):
    app = Sanic(__name__)
    if test:
        app.config['TESTING'] = True
    app.config.from_object(Config)
    register_blueprints(app)
    return app


def register_blueprints(app):
    from ChartRobot.views.hello import blueprint as hellp_bp
    app.register_blueprint(hellp_bp)

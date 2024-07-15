from flask import Flask

def configure_urls(app: Flask):
    from apps.users.urls import user_blueprint
    from apps.market.urls import market_blueprint

    app.register_blueprint(user_blueprint, url_prefix='/users')
    app.register_blueprint(market_blueprint, url_prefix='/markets')

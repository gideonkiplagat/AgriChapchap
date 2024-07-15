from flask import jsonify, request
from . import market_blueprint
from .models import Market
from agrichap.agrichap import db

@market_blueprint.route('/', methods=['GET'])
def get_markets():
    markets = Market.query.all()
    return jsonify([market.product_name for market in markets]), 200

@market_blueprint.route('/', methods=['POST'])
def create_market():
    data = request.get_json()
    new_market = Market(product_name=data['product_name'], price=data['price'])
    db.session.add(new_market)
    db.session.commit()
    return jsonify({'message': 'Market created successfully'}), 201

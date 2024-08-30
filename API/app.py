from flask import Flask , jsonify, request as flask_request
from flask_restful import Api
import json
import typing
from purchase_orders.resources import PurchaseOrders
from purchase_orders.resources import PurchaseOrderById
from purchase_orders_items.resources import PurchaseOrdersItems
from db import db


def create_app() -> Flask:#defining the Json typei
    app=Flask(import_name=__name__)
    api=Api(app=app)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:max123@localhost:5432/python_api'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    @app.before_request
    def create_tables():
        app.before_request_funcs[None].remove(create_tables)
        db.create_all()

    api.add_resource(PurchaseOrders,'/purchase_orders')
    api.add_resource(PurchaseOrderById,'/purchase_orders/<int:id>')
    api.add_resource(PurchaseOrdersItems,'/purchase_orders/<int:id>/items')
    return app
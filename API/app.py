from flask import Flask , jsonify, request as flask_request
from flask_restful import Api
import json
import typing
from purchase_orders.resources import PurchaseOrders
from purchase_orders.resources import PurchaseOrderById
from purchase_orders_items.resources import PurchaseOrdersItems


def create_app() -> Flask:#defining the Json typei
    app=Flask(import_name=__name__)
    api=Api(app=app)
    api.add_resource(PurchaseOrders,'/purchase_orders')
    api.add_resource(PurchaseOrderById,'/purchase_orders/<int:id>')
    api.add_resource(PurchaseOrdersItems,'/purchase_orders/<int:id>/items')
    return app
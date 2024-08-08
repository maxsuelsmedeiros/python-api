from flask import Flask , jsonify, request as flask_request
from flask_restful import Api
import json
import typing

#defining the Json type
type json = json
app=Flask(__name__)
api=Api(app)
from purchase_orders.resources import PurchaseOrders,PurchaseOrdersById
from purchase_orders_items.resources import PurchaseOrdersItems


api.add_resource(PurchaseOrders,'/purchase_orders')
api.add_resource(PurchaseOrdersById,'/purchase_orders/<int:id>')
api.add_resource(PurchaseOrdersItems, '/purchase_orders/<int:id>/items')

app.run(port=5000)

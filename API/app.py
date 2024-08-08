from flask import Flask , jsonify, request as flask_request
from flask_restful import Api
import json
import typing

#defining the Json type
type json = json
app=Flask(__name__)
api=Api(app)
from purchase_orders.resources import PurchaseOrders


api.add_resource(PurchaseOrders,'/purchase_orders')

app.run(port=5000)

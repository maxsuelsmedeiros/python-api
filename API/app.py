from flask import Flask , jsonify, request as flask_request
from flask_restful import Api,Resource
import json
import typing

#defining the Json type
type json = json
app=Flask(__name__)
api=Api(app)


global purchase_orders 
purchase_orders: json= [
    {
        'id':1,
        'description':'purchase order 1',
        'items':[
            {'id':1,
            'description': 'purchase order 1',
            'price':20.99
            }
        ]

    }
]

class PurchaseOrders(Resource):
    def get(self) -> json:
        return jsonify(purchase_orders)

api.add_resource(PurchaseOrders,'/purchase_orders')

app.run(port=5000)
from flask import jsonify
from flask_restful import Resource, reqparse
import json

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

    parser = reqparse.RequestParser()
    parser.add_argument(
        'id',
        type=int,
        required=True,
        help='Inform an ID to proceed!'
    )

    parser.add_argument(
        'description',
        type =str,
        required = True,
        help = 'Add a description to the purchase!'
    )

    def get(self) -> json:
        return jsonify(purchase_orders)
    
    def post(self) -> json:
        request_to_add: json = PurchaseOrders().parser.parse_args()
        purchase_order: json = {
                "id": request_to_add["id"],
                "description": request_to_add["description"],
                "items": []
            }
        # adding the purchase order in the purchase_orders
        purchase_orders.append(purchase_order)
        return jsonify(purchase_order)

class PurchaseOrdersById(Resource):

    def get(self,id):
        for purchase in purchase_orders:
            if purchase['id'] == id:
                return jsonify(purchase['items'])

        return jsonify({'message':'Pedido {} não encontrado'.format(id)})
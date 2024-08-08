from flask_restful import Resource,reqparse
from flask import jsonify
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

class PurchaseOrdersItems(Resource):
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
    parser.add_argument(
        'price',
        type = float,
        required = True,
        help = 'Add a description to the purchase!'
    )
    def get(self):
        for purchase in purchase_orders:
            if purchase['id'] == id:
                return jsonify(purchase['items'])

        return jsonify({'message':'Pedido {} não encontrado'.format(id)})
    def post(self,id)-> json:
        request_to_post: json = PurchaseOrdersItems().parser.parse_args()
        for purchase in purchase_orders:
            if purchase['id'] == id:
                purchase['items'].append({
                    'id':request_to_post['id'],
                    'description':request_to_post['description'],
                    'value': request_to_post['price']
                })
                return jsonify(purchase)
        # adding the purchase order in the purchase_orders
        return jsonify({'message':'O Pedido número:{} não foi encontrado'.format(req)})
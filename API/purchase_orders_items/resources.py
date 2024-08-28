from flask import jsonify
from flask_restful import Resource,reqparse
from typing import Union, Dict, List,Any,Type


JSON = Union[Dict[str, Any], List[Any], int, str, float, bool, Type[None]]
global purchase_orders 
purchase_orders: JSON= [
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
        type = int,
        required = True,
        help = 'Inform a valid ID!'
    )

    parser.add_argument(
        'description',
        type = str,
        required = True,
        help = 'Inform a valid Description!'
    )

    parser.add_argument(
        'price',
        type = float,
        required = True,
        help = 'Inform a valid price!'
    )

    def get(self,id):
        for purchase in purchase_orders:
            if purchase['id'] == id:
                return jsonify(purchase['items'])
        return jsonify({'message':'Id number {} not found! Try other one!'.format(id)})
    
    def post(self,id):
        data = PurchaseOrdersItems.parser.parse_args()

        for purchase in purchase_orders:
            if purchase['id'] == id:
                purchase['items'].append(
                    {
                        'id': data['id'],
                        'description': data['description'],
                        'price': data['price']
                    }
                )
                return jsonify(purchase)
        return jsonify({'message':'Id number {} not found! Try other one!'.format(id)})

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

class PurchaseOrders(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        'id',
        type = int,
        required = True,
        help='Id not valid, inform a new one!'
    )

    parser.add_argument(
        'description',
        type = str,
        required = True,
        help='Description not valid, inform a new one!'
    )


    def get(self)-> JSON:
        return jsonify(purchase_orders)
    
    def post(self)-> JSON:
        data = PurchaseOrders.parser.parse_args()
        purchase_order = {
            'id': data['id'],
            'description': data['description'],
            'items': []
        }
        purchase_orders.append(purchase_order)

        return jsonify(purchase_order)
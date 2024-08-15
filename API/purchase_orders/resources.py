from flask import jsonify
from flask_restful import Resource
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
    def get(self)-> JSON:
        return jsonify(purchase_orders)
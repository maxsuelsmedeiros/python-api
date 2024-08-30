from flask import jsonify
from flask_restful import Resource,reqparse
from typing import Union, Dict, List,Any,Type
from .model import PurchaseOrderModel

JSON = Union[Dict[str, Any], List[Any], int, str, float, bool, Type[None]]


class PurchaseOrders(Resource):
    parser = reqparse.RequestParser()

    parser.add_argument(
        'description',
        type = str,
        required = True,
        help='Description not valid, inform a new one!'
    )


    def get(self)-> JSON:
        purchase_orders = PurchaseOrderModel.find_all()
        return [p.as_dict() for p in purchase_orders]
    
    def post(self)-> JSON:
        data = PurchaseOrders.parser.parse_args()
        purchase_order = PurchaseOrderModel(**data)
        purchase_order.save()

        return purchase_order.as_dict()
    
class PurchaseOrderById(Resource):

    def get(self,id: int):
        purchase_order = PurchaseOrderModel.find_by_id(id)
        if purchase_order:
            return purchase_order.as_dict()
        return jsonify({'message':'Id: "{}" not valid, inform a new one!'.format(id)})

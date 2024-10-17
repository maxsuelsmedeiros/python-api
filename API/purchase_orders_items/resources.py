from flask import jsonify
from flask_restful import Resource,reqparse
from typing import List,Dict
from .model import PurchaseOrdemItemsModel
from purchase_orders.model import PurchaseOrderModel 

class PurchaseOrdersItems(Resource):

    parser = reqparse.RequestParser()

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

    def get(self,id)-> List[Dict]:
        purchase_order_item = PurchaseOrdemItemsModel.find_by_purchase_order_id(id)
        return [p.as_dict() for p in purchase_order_item]
    
    def post(self,id):
        purchase_order = PurchaseOrderModel.find_by_id(id)
        if purchase_order:
            data = PurchaseOrdersItems.parser.parse_args()
            data['purchase_order_id'] = id
            purchase_orders_item = PurchaseOrdemItemsModel(**data)
            purchase_orders_item.save()
            return purchase_orders_item.as_dict()
        return jsonify({'message':'Id number {} not found! Try other one!'.format(id)})

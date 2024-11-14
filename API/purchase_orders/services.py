from .model import PurchaseOrderModel
from typing import DefaultDict
from flask import jsonify
import json

class PurchaseOrdersService:

    def find_all(self)-> DefaultDict:
        purchase_orders = PurchaseOrderModel.find_all()

        return [p.as_dict() for p in purchase_orders]

    def create(self,**kwargs) -> DefaultDict:
        purchase_order = PurchaseOrderModel(**kwargs)
        purchase_order.save()

        return purchase_order.as_dict()

    def find_by_id(self,id)-> json:
        purchase_order = PurchaseOrderModel.find_by_id(id)
        if purchase_order:
            return purchase_order.as_dict()
        return jsonify({'message':'Id: "{}" not valid, inform a new one!'.format(id)})
from flask_restful import Resource,reqparse
from typing import Union, Dict, List,Any,Type
from .services import PurchaseOrdersService

JSON = Union[Dict[str, Any], List[Any], int, str, float, bool, Type[None]]


class PurchaseOrders(Resource):
    __service__ = PurchaseOrdersService()
    parser = reqparse.RequestParser()

    parser.add_argument(
        'description',
        type = str,
        required = True,
        help='Description not valid, inform a new one!'
    )

    parser.add_argument(
        'quantity',
        type = int,
        required = True,
        help = 'Inform a quantity!'
    )

    def get(self)-> JSON:
        return self.__service__.find_all()
    
    def post(self)-> JSON:
        data = PurchaseOrders.parser.parse_args()
        return self.__service__.create(**data)
    
class PurchaseOrderById(Resource):

    __service__ = PurchaseOrdersService()

    def get(self,id: int) -> any:
        return self.__service__.find_by_id(id=id)
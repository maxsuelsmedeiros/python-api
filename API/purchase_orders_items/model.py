from db import db
from typing import Dict

class PurchaseOrdemItemsModel(db.Model):
    __tablename__ = 'purchase_orders_items'

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(500), nullable=False)
    price = db.Column(db.Float(precision=2), nullable=False)
    purchase_order_id = db.Column(db.Integer, db.ForeignKey('purchase_order.id'), nullable = False)

    def __init__ (self, description : str , price : float, purchase_order_id : int) -> None:
        self.description = description
        self.price = price
        self.purchase_order_id = purchase_order_id

    def as_dict(self) -> Dict:
        return {c.name: getattr(self,c.name) for c in self.__table__.columns}
    
    @classmethod
    def find_by_purchase_order_id(cls, _purchase_order_id) -> any:
        return cls.query.filter_by(purchase_order_id=_purchase_order_id).all()
    
    def save(self)-> None:
        db.session.add(self)
        db.session.commit()
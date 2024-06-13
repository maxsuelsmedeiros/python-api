from flask import Flask,jsonify
import json
import typing

#defining the Json type
type json = json
app=Flask(__name__)

purchase_orders: json = [
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

#GET purchase_orders
#GET purchase_orders_by_id
#POST purchase_orders
#GET purchase_orders_items
#POST purchase_orders_item

@app.route(rule='/')
def home() -> str:
    return 'Hello Beautiful World!'

@app.route(rule='/purchase_orders')
def get_purchase_orders() -> jsonify:
    return jsonify(purchase_orders)

@app.route(rule='/purchase_orders/<int:id>')
def get_purchase_orders_by_id(id) -> json|str:
    for purchase_item in purchase_orders:
        if purchase_item['id']==id:
            return jsonify(purchase_item)
    return jsonify({'message':'The ID passed:{} is not valid, review it and try again!'.format(id)})



app.run(port=5000)
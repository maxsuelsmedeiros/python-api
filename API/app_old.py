from flask import Flask , jsonify, request as flask_request
import json
import typing

#defining the Json type
type json = json
app=Flask(__name__)


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

#GET purchase_orders
#GET purchase_orders_by_id
#POST purchase_orders
#GET purchase_orders_items
#POST purchase_orders_item

@app.route(rule='/')
def home() -> str:
    return 'Hello Beautiful World!'

@app.route(rule='/purchase_orders')
def get_purchase_orders() -> json:
    return jsonify(purchase_orders)

@app.route(rule='/purchase_orders/<int:id>')
def get_purchase_orders_by_id(id:str) -> json:
    for purchase_item in purchase_orders:
        if purchase_item['id']==id:
            return jsonify(purchase_item)
    return jsonify({'message':'The ID passed:{} is not valid, review it and try again!'.format(id)})

@app.route('/purchase_orders', methods=['POST'])
def create_purchase_order() -> json:
    request_to_add: json = flask_request.get_json()
    if request_to_add['items'] != []:
        purchase_order: json = {
            "id": request_to_add["id"],
            "description": request_to_add["description"],
            "items": [{
                "id":request_to_add["items"][0]["id"],
                "description":request_to_add["items"][0]["description"],
                "value":request_to_add["items"][0]["value"]
            }]
        }
    else:
        purchase_order: json = {
            "id": request_to_add["id"],
            "description": request_to_add["description"]
        }
    # adding the purchase order in the purchase_orders
    purchase_orders.append(purchase_order)
    return jsonify(purchase_order)

@app.route(rule='/purchase_orders/<int:id>/items')
def get_purchase_orders_items(id:str) -> json:
    for purchase in purchase_orders:
        if purchase['id'] == id:
            return jsonify(purchase['items'])

    return jsonify({'message':'Pedido {} não encontrado'.format(id)})


@app.route(rule='/purchase_orders/<int:id>/items',methods=['POST'])
def POST_purchase_orders_items(id:str) -> json:
    new_item_data : json = flask_request.get_json()
    for purchase in purchase_orders:
        if purchase['id'] == id:
            purchase['items'].append({
                'id':new_item_data['id'],
                'description':new_item_data['description'],
                'value': new_item_data['price']
            })
            return jsonify(purchase)

    return jsonify({'message':'Pedido {} não encontrado'.format(id)})
app.run(port=5000)
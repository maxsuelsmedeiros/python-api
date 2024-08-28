import json

def test_get_items_by_purchase_order_id(test_client):
    response = test_client.get('/purchase_orders/1/items')

    assert response.status_code == 200
    assert len(response.json) == 1
    assert response.json[0]['id'] == 1
    assert response.json[0]['description'] == 'purchase order 1'
    assert response.json[0]['price'] ==20.99

def test_get_items_by_purchase_order_id_not_found(test_client):
    id = 9999
    response = test_client.get('/purchase_orders/{}/items'.format(id))

    assert response.status_code == 200
    assert response.json['message'] == 'Id number {} not found! Try other one!'.format(id)
    
def test_post_purchase_order_item(test_client):
    obj = {
        'id':1,
        'description':'Boxing gloves',
        'price' : 50.99
    }

    response = test_client.post(
        '/purchase_orders/1/items',
        data = json.dumps(obj),
        content_type = 'application/json'
    )

    assert response.status_code == 200
    assert response.json['id'] == 1
    assert len(response.json['items']) == 2
    assert response.json['items'][1]['id'] == obj['id']
    assert response.json['items'][1]['description'] == obj['description']
    assert response.json['items'][1]['price'] == obj['price']

def test_post_invalid_id(test_client):
    obj = {
        'description':'Boxing gloves',
        'price' : 50.99
    }

    response = test_client.post(
        '/purchase_orders/1/items',
        data = json.dumps(obj),
        content_type = 'application/json'
    )

    assert response.status_code == 400
    assert response.json['message']['id'] == 'Inform a valid ID!'

def test_post_invalid_description(test_client):
    obj = {
        'id':1,
        'price' : 50.99
    }

    response = test_client.post(
        '/purchase_orders/1/items',
        data = json.dumps(obj),
        content_type = 'application/json'
    )

    assert response.status_code == 400
    assert response.json['message']['description'] == 'Inform a valid Description!'

def test_post_invalid_price(test_client):
    obj = {
        'id':1,
        'description':'Boxing gloves'
    }

    response = test_client.post(
        '/purchase_orders/1/items',
        data = json.dumps(obj),
        content_type = 'application/json'
    )

    assert response.status_code == 400
    assert response.json['message']['price'] == 'Inform a valid price!'

def test_post_insert_invalid_id(test_client):
    obj = {
        'id':9999,
        'description':'Boxing gloves',
        'price': 50.99
    }

    response = test_client.post(
        '/purchase_orders/{}/items'.format(obj['id']),
        data = json.dumps(obj),
        content_type = 'application/json'
    )

    assert response.json['message']== 'Id number {} not found! Try other one!'.format(obj['id'])

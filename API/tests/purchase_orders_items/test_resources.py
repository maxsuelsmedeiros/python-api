import json

def test_get_items_by_purchase_order_id(test_client,seed_db):
    response = test_client.get('/purchase_orders/{}/items'.format(seed_db['purchase_order'].id))

    assert response.status_code == 200
    assert len(response.json) == 1
    assert response.json[0]['id'] == seed_db['items'].id
    assert response.json[0]['description'] == seed_db['items'].description
    assert response.json[0]['price'] == seed_db['items'].price

def test_get_items_by_purchase_order_id_not_found(test_client):
    id = 9999
    response = test_client.get('/purchase_orders/{}/items'.format(id))

    assert response.status_code == 200
    assert response.json['message'] == 'Id number {} not found! Try other one!'.format(id)
    
def test_post_purchase_order_item(test_client,seed_db):
    obj = {
        'description':'Boxing gloves',
        'price' : 50.99
    }

    response = test_client.post(
        '/purchase_orders/{}/items'.format(seed_db['purchase_order'].id),
        data = json.dumps(obj),
        content_type = 'application/json'
    )

    assert response.status_code == 200
    assert response.json['id'] is not None
    assert response.json['description'] == obj['description']
    assert response.json['price'] == obj['price']


def test_post_invalid_description(test_client,seed_db):
    obj = {
        'price' : 50.99
    }

    response = test_client.post(
        '/purchase_orders/{}/items'.format(seed_db['purchase_order'].id),
        data = json.dumps(obj),
        content_type = 'application/json'
    )

    assert response.status_code == 400
    assert response.json['message']['description'] == 'Inform a valid Description!'

def test_post_invalid_price(test_client,seed_db):
    obj = {
        'description':'Boxing gloves'
    }

    response = test_client.post(
        '/purchase_orders/{}/items'.format(seed_db['purchase_order'].id),
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

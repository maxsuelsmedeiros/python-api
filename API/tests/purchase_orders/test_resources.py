import json

def test_get_purchase_orders(test_client,seed_db):
    response = test_client.get('/purchase_orders')

    assert response.status_code == 200
    assert response.json[0]['id'] == seed_db.id
    assert response.json[0]['description']== seed_db.description
    
def test_post_purchase_orders(test_client):
    obj: dict = {'description':'Purchase Order id 2'}

    response = test_client.post(
        '/purchase_orders',
        data=json.dumps(obj),
        content_type = 'application/json'
    )

    assert response.status_code == 200
    assert response.json['id'] is not None
    assert response.json['description'] == obj['description']

def test_post_empty_description(test_client) -> None:
    response = test_client.post(
        '/purchase_orders',
        data = json.dumps({}),
        content_type = 'application/json'
    )

    assert response.status_code == 400
    assert response.json['message']['description'] == 'Description not valid, inform a new one!'

def test_get_purchase_order_by_id(test_client,seed_db)-> None:
    response = test_client.get('/purchase_orders/{}'.format(seed_db.id))

    assert response.status_code == 200
    assert response.json['id'] == seed_db.id
    assert response.json['description'] == seed_db.description

def test_get_purchase_order_not_found(test_client)-> None:
    id : int = 9999
    response = test_client.get('/purchase_orders/{}'.format(id))

    assert response.status_code == 200
    assert response.json['message'] == 'Id: "{}" not valid, inform a new one!'.format(id)


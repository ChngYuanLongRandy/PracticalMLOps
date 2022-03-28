import pytest
from ...app import create_app
from flask import json

app = create_app()

def test_addemployee():        
    response = app.test_client().post(
        '/',
        data=json.dumps({
            "name":"Randy",
            "rank":"boss",
            "pay":"soso"
        }),
        content_type='application/json',
    )

    data = json.loads(response.get_data(as_text=True))

    assert response.status_code == 201
    assert data['name'] == 'Randy'
    assert data['rank'] == 'boss'
    assert data['pay'] == 'soso'

def test_addemployee2():        
    response = app.test_client().post(
        '/',
        data=json.dumps({
            "name":"Wong Wan Mun",
            "rank":"boss",
            "pay":"Good"
        }),
        content_type='application/json',
    )

    data = json.loads(response.get_data(as_text=True))

    assert response.status_code == 201
    assert data['name'] == 'Wong Wan Mun'
    assert data['rank'] == 'boss'
    assert data['pay'] == 'Good'

def test_addemployee3():        
    response = app.test_client().post(
        '/',
        data=json.dumps({
            "name":"James",
            "rank":"Peon",
            "pay":"Okay"
        }),
        content_type='application/json',
    )

    data = json.loads(response.get_data(as_text=True))

    assert response.status_code == 201
    assert data['name'] == 'James'
    assert data['rank'] == 'Peon'
    assert data['pay'] == 'Okay'

def test_get_employees():
    response = app.test_client().get('/')

    assert response.status_code == 200

    data = json.loads(response.data)

    assert len(data['data']) == 3
    assert data['data'][0]['name'] == 'Randy'
    assert data['data'][1]['name'] == 'Wong Wan Mun'
    assert data['data'][2]['name'] == 'James'

def test_get_1st_emp():
    response = app.test_client().get('/1')
    
    assert response.status_code == 200

    data = json.loads(response.get_data(as_text=True))

    assert data['name'] == 'Randy'
    assert data['rank'] == 'boss'
    assert data['pay'] == 'soso'


def test_deactivate_1st_emp():
    response = app.test_client().delete('/1/active')
    
    assert response.status_code == 200


def test_get_employees_2():
    response = app.test_client().get('/')

    assert response.status_code == 200

    data = json.loads(response.data)

    assert len(data['data']) == 2
    assert data['data'][0]['name'] == 'Wong Wan Mun'
    assert data['data'][1]['name'] == 'James'

def test_reactivate_1st_emp():
    response = app.test_client().put('/1/active')
    
    assert response.status_code == 200

def test_get_employees_3():
    response = app.test_client().get('/')

    assert response.status_code == 200

    data = json.loads(response.data)

    assert len(data['data']) == 3
    assert data['data'][0]['name'] == 'Randy'
    assert data['data'][1]['name'] == 'Wong Wan Mun'
    assert data['data'][2]['name'] == 'James'


def test_get_health():
    response = app.test_client().get('/health')

    data = json.loads(response.get_data(as_text=True))

    assert data['message'] == 'health OK'
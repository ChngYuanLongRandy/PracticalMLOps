import pytest

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
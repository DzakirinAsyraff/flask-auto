import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_home(client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.get_json() == {'message': 'Hello, World!'}

def test_sum(client):
    response = client.get('/sum/3/4')
    assert response.status_code == 200
    assert response.get_json() == {'result': 7}

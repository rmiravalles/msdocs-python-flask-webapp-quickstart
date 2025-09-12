import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index_page(client):
    """Test the index page loads correctly"""
    rv = client.get('/')
    assert rv.status_code == 200

def test_favicon(client):
    """Test favicon.ico is accessible"""
    rv = client.get('/favicon.ico')
    assert rv.status_code == 200

def test_hello_with_name(client):
    """Test /hello route with a name"""
    rv = client.post('/hello', data={'name': 'John'})
    assert rv.status_code == 200
    assert b'John' in rv.data

def test_hello_without_name(client):
    """Test /hello route without a name (should redirect)"""
    rv = client.post('/hello', data={})
    assert rv.status_code == 302  # Redirect status code
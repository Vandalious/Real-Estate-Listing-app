import requests

import pytest
from httpx import AsyncClient

from main import app

from config import Config


token = ''

def get_token():
    global token
    response = requests.post(
        'http://localhost:8000/auth/token/',
        data={'username': Config.SUPERUSER_USERNAME, 'password': Config.SUPERUSER_PASSWORD}
    )
    token = response.json()['access_token']
    return token


@pytest.mark.anyio
async def test_homepage():
    async with AsyncClient(app=app, base_url='http://test') as ac:
        response = await ac.get('/')
    assert response.status_code == 200
    assert response.json() == {'Message': 'Welcome to the homepage'}


# @pytest.mark.anyio
# async def test_login():
#     # global token
#     async with AsyncClient(app=app, base_url='http://test') as ac:
#         response = await ac.post(
#             'api/v1/auth/token/',
#             data={'username': 'arash', 'password': 'OoffoO123'}
#         )
#     assert response.status_code == 200
#     # return response['id']


# def test_get_all_users():
#     # sleep(1)
#     token = get_token()
#     print('token:', token)
#     headers = {'Authorization': f'Bearer {token}'}
#     response = client.get(
#         '/users/getAll/',
#         headers=headers)
#     assert response.status_code == 200


@pytest.mark.anyio
async def test_get_all_listings():
    async with AsyncClient(app=app, base_url='http://test') as ac:
        response = await ac.get('api/v1/listings/getAllListings/')
    assert response.status_code == 200


# def test_read_item():
#     response = client.get('/items/foo', headers={'X-Token': 'coneofsilence'})
#     assert response.status_code == 200
#     assert response.json() == {
#         'id': 'foo',
#         'title': 'Foo',
#         'description': 'There goes my hero',
#     }


# def test_read_item_bad_token():
#     response = client.get('/items/foo', headers={'X-Token': 'hailhydra'})
#     assert response.status_code == 400
#     assert response.json() == {'detail': 'Invalid X-Token header'}


# def test_read_inexistent_item():
#     response = client.get('/items/baz', headers={'X-Token': 'coneofsilence'})
#     assert response.status_code == 404
#     assert response.json() == {'detail': 'Item not found'}


# def test_create_item():
#     response = client.post(
#         '/items/',
#         headers={'X-Token': 'coneofsilence'},
#         json={'id': 'foobar', 'title': 'Foo Bar', 'description': 'The Foo Barters'},
#     )
#     assert response.status_code == 200
#     assert response.json() == {
#         'id': 'foobar',
#         'title': 'Foo Bar',
#         'description': 'The Foo Barters',
#     }


# def test_create_item_bad_token():
#     response = client.post(
#         '/items/',
#         headers={'X-Token': 'hailhydra'},
#         json={'id': 'bazz', 'title': 'Bazz', 'description': 'Drop the bazz'},
#     )
#     assert response.status_code == 400
#     assert response.json() == {'detail': 'Invalid X-Token header'}


# def test_create_existing_item():
#     response = client.post(
#         '/items/',
#         headers={'X-Token': 'coneofsilence'},
#         json={
#             'id': 'foo',
#             'title': 'The Foo ID Stealers',
#             'description': 'There goes my stealer',
#         },
#     )
#     assert response.status_code == 400
#     assert response.json() == {'detail': 'Item already exists'}

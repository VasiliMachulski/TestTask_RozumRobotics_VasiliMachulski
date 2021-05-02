import requests
import logging

positive_bear_types = ['POLAR', 'BROWN', 'BLACK', 'GUMMY']
negative_bear_types = ['brown', 'браун', 1, 1.6, 0, -1, '!@#$%^&*()']
positive_bear_name = ['Misha', 'Миша', 123, 123.1, -123, '!@$%^']
positive_bear_age = [1, 1.1, '12', '1.3']
negative_bear_age = [0, -1, 'age', 'лет', '!@#$']
baseUrl = 'http://localhost:8091/bear'


def test_creating_positive_types_bear():
    for i in positive_bear_types:
        response = requests.post(url=baseUrl,
                                 json={"bear_type": i,
                                       "bear_name": 'sasha',
                                       "bear_age": 22})
        assert response.status_code == 200, f'Response code = {response}'


def test_creating_negative_types_bear():
    for i in negative_bear_types:
        response = requests.post(url=baseUrl,
                                 json={"bear_type": i,
                                       "bear_name": 'sasha',
                                       "bear_age": 22})

        assert response.status_code == 400, f'Response code = {response}, bear_type = {i}'


def test_creating_bear_name():
    for i in negative_bear_types:
        response = requests.post(url=baseUrl,
                                 json={"bear_type": 'BROWN',
                                       "bear_name": i,
                                       "bear_age": 22})

        assert response.status_code == 200, f'Response code = {response}'


# Нужен ли тест где проверяется медведь без возраста?
def test_creating_bear_age():
    for i in positive_bear_age:
        response = requests.post(url=baseUrl,
                                 json={"bear_type": 'BROWN',
                                       "bear_name": 'sasha',
                                       "bear_age": i})

        assert response.status_code == 200, f'Response code = {response}'


def test_creating_negative_bear_age():
    for i in negative_bear_age:
        response = requests.post(url=baseUrl,
                                 json={"bear_type": 'BROWN',
                                       "bear_name": 'sasha',
                                       "bear_age": i})
        assert response.status_code == 400, f'Response code = {response}, bear_type = {i}'


def test_read_all_bears():
    response = requests.get(url=baseUrl)

    assert response.status_code == 200, f'Response code = {response}'


def test_delete_all_bear():
    response = requests.post(url=baseUrl,
                             json={"bear_type": 'BROWN',
                                   "bear_name": 'Example',
                                   "bear_age": 22})
    response = requests.delete(url=baseUrl)
    assert response.status_code == 200, f'Response code = {response}'

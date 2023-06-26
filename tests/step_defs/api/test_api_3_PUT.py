import ast
import json
import pytest
import requests

from pytest_bdd import (given, scenario, then, when, parsers)


# @pytest.mark.skip
@pytest.mark.api
@pytest.hookimpl(tryfirst=True)
@scenario('../../../tests/features/api/api_PUT.feature', 'PUT Books API')
def test_api_PUT():
    """PUT API test"""


@given('I am a sample PUT API')
def test_base_api_url():
    global api_url
    api_url = 'http://localhost:3000'


@when(parsers.parse('I set header param request content type as "{header_content_type}"'))
def set_header_without_request_body(header_content_type):
    global content_type
    content_type = header_content_type


@when(parsers.parse('I set "{request_type}" method and send the request'))
def set_get_api_endpoint(request_type):
    global get_api_endpoint
    get_api_endpoint = api_url + '/books'
    if request_type == "GET":
        response = requests.get(url=get_api_endpoint,
                                headers={"Content-Type": f"{content_type}", "charset": "UTF-8"})
        global get_response
        get_response = response.json()
        # print("get_response: {}".format(get_response))

        global first_book_id
        # first_book = get_response["books"][0]
        first_book_id = get_response["books"][0]['id']


@when(parsers.parse('I send "{request_type}" HTTP request with "{payload}"'))
def send_put_request(request_type, payload):
    global put_api_endpoint
    put_api_endpoint = api_url + f'/books/{first_book_id}'
    if request_type == "PUT":
        response = requests.put(url=put_api_endpoint,
                                data=json.dumps(ast.literal_eval(payload)),
                                headers={"Content-Type": "application/json", "charset": "UTF"})
        global put_response
        put_response = response.json()
        # print("put_response: {}".format(put_response))

        global put_status_code
        put_status_code = response.status_code


@then(parsers.parse('I set "{request_type}" method and send the request'))
def set_get_api_endpoint(request_type):
    global get_api_endpoint
    get_api_endpoint = api_url + '/books'
    if request_type == "GET":
        response = requests.get(url=get_api_endpoint,
                                headers={"Content-Type": f"{content_type}", "charset": "UTF-8"})
        updated_get_response = response.json()
        global updated_author
        updated_author = updated_get_response["books"][0]['author']


@pytest.hookimpl(trylast=True)
@then(parsers.parse('I receive valid HTTP response code "{status_code}" for "{request_type}" and expect response body '
                    'is non-empty'))
def validate_request(status_code, request_type):
    if request_type == "PUT":
        assert put_status_code == int(status_code)
        assert updated_author == "Saad1"
        assert put_response is not None

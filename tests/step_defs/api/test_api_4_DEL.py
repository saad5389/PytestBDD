import pytest
import requests

from pytest_bdd import (given, scenario, then, when, parsers)


# @pytest.mark.skip
@pytest.mark.api
@pytest.hookimpl(tryfirst=True)
@scenario('../../../tests/features/api/api_DEL.feature', 'DELETE Books API')
def test_api_DELETE():
    """DELETE API test"""


@given('I am a sample DELETE API')
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
        get_response = response.json()
        global first_book_id
        first_book_id = get_response["books"][0]['id']


@when(parsers.parse('I set "{request_type}" method and send the request to get Auth token'))
def set_post_api_endpoint(request_type):
    if request_type == "POST":
        global post_api_endpoint
        post_api_endpoint = api_url + '/books/authToken'
        print('POST ENDPOINT URL: {}'.format([post_api_endpoint]))

        response = requests.post(url=post_api_endpoint,
                                 headers={"Content-Type": f"{content_type}", "charset": "UTF"})
        post_response = response.json()

        global auth_token
        auth_token = post_response["jwtToken"]


@when(parsers.parse('I send "{request_type}" HTTP request to delete a record'))
def send_delete_request(request_type):
    global delete_api_endpoint
    delete_api_endpoint = api_url + f'/books/{first_book_id}'
    if request_type == "DELETE":
        response = requests.delete(url=delete_api_endpoint,
                                   headers={"Content-Type": f"{content_type}", "charset": "UTF", "authorization": f"{auth_token}"})
        global delete_response
        delete_response = response.json()
        print("delete_response: {}".format(delete_response))

        global delete_status_code
        delete_status_code = response.status_code


@then(parsers.parse('I set "{request_type}" method and send the request'))
def set_get_api_endpoint(request_type):
    global get_api_endpoint
    get_api_endpoint = api_url + '/books'
    if request_type == "GET":
        response = requests.get(url=get_api_endpoint,
                                headers={"Content-Type": f"{content_type}", "charset": "UTF-8"})
        get_response = response.json()
        global book_id
        book_id = get_response["books"][0]['id']


@pytest.hookimpl(trylast=True)
@then(parsers.parse('I receive valid HTTP response code "{status_code}" for "{request_type}" and expect response body '
                    'is non-empty'))
def validate_request(status_code, request_type):
    if request_type == "DELETE":
        assert delete_status_code == int(status_code)
        assert first_book_id != book_id

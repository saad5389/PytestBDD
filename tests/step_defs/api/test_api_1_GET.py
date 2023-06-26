import pytest
import requests

from pytest_bdd import (given, scenario, then, when, parsers)


# @pytest.mark.skip
@pytest.mark.api
@pytest.hookimpl(tryfirst=True)
@scenario('../../../tests/features/api/api_GET.feature', 'GET Books API')
def test_api_GET():
    """GET API test"""


@given('I am a sample GET API')
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
        print("get_response: {}".format(get_response))
        global get_status_code
        get_status_code = response.status_code
        global get_books_id
        get_books_id = get_response["books"][0]['id']


@pytest.hookimpl(trylast=True)
@then(parsers.parse('I receive valid HTTP response code "{status_code}" for "{request_type}" and expect response body is non-empty'))
def validate_request(status_code, request_type):
    if request_type == "GET":
        print(get_status_code)
        assert get_status_code == int(status_code)
        assert get_response is not None
        assert type(get_books_id) == int

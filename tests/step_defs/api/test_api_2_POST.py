import ast
import json
import pytest
import requests

from pytest_bdd import (given, scenario, then, when, parsers)


# @pytest.mark.skip
@pytest.mark.api
@pytest.hookimpl(tryfirst=True)
@scenario('../../../tests/features/api/api_POST.feature', 'POST Books API')
def test_api_POST():
    """POST API test"""


@given('I am a sample POST API')
def test_base_api_url():
    global api_url
    api_url = 'http://localhost:3000'


@when(parsers.parse('I set header param request content type as "{header_content_type}"'))
def set_header_without_request_body(header_content_type):
    global content_type
    content_type = header_content_type


@when(parsers.parse('I set "{request_type}" method and send the request with "{payload}"'))
def set_post_api_endpoint(request_type, payload):
    global post_api_endpoint
    post_api_endpoint = api_url + '/books'
    if request_type == "POST":
        response = requests.post(url=post_api_endpoint,
                                 data=json.dumps(ast.literal_eval(payload)),
                                 headers={"Content-Type": f"{content_type}", "charset": "UTF"})
        global post_response
        post_response = response.json()
        print("post_response: {}".format(post_response))

        global post_status_code
        post_status_code = response.status_code


@then(parsers.parse('I set "{request_type}" method and send the request'))
def set_get_api_endpoint(request_type):
    global get_api_endpoint
    get_api_endpoint = api_url + '/books'
    if request_type == "GET":
        response = requests.get(url=get_api_endpoint,
                                headers={"Content-Type": f"{content_type}", "charset": "UTF-8"})
        updated_get_response = response.json()
        global created_author
        created_author = updated_get_response["books"][-1]['author']


@pytest.hookimpl(trylast=True)
@then(parsers.parse('I receive valid HTTP response code "{status_code}" for "{request_type}"'))
def validate_request(status_code, request_type):
    if request_type == "POST":
        assert post_status_code == int(status_code)
        assert created_author == "Saad5389"
        assert post_response is not None

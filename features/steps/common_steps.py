from behave import when, then
from hamcrest import assert_that, equal_to
from common import test


@when("I set request url '{req_url}'")
def step_impl(context, req_url):
    context.request_url = test.REQ_URLS.get(req_url)


@when("I set request method '{req_method}'")
def step_impl(context, req_method):
    context.request_method = req_method


@when("I send request")
def step_impl(context):
    if not hasattr(context, "store_name"):
        context.store_name = None
    response = test.make_request(context.request_method, test.make_url(context.request_url, context.store_name))
    context.response = response


@then("I get response code '{code:d}'")
def step_impl(context, code):
    assert_that(context.response.status_code, equal_to(code))

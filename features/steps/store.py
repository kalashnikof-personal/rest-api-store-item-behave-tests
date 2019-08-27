from behave import step, when, then
from hamcrest import assert_that, equal_to, has_item, instance_of, has_key

from common import test


@when("I set store name")
def step_impl(context):
    context.store_name = test.generate_random_str()


@then("I get correct response body for add store")
def step_impl(context):
    expected = {
        "name": context.store_name,
        "items": [],
    }
    assert_that(context.response.json(), equal_to(expected))


@then("I get store in list of stores")
def step_impl(context):
    stores = test.make_request(test.METHOD_GET, test.make_url(test.REQ_URLS["stores"]))
    expected = {
        "name": context.store_name,
        "items": [],
    }
    assert_that(stores.json()["stores"], has_item(expected))


@then("I get correct store already exists message")
def step_impl(context):
    expected = {"message": f"A store with name {context.store_name} already exists."}
    assert_that(context.response.json(), equal_to(expected))


@then("I get correct response body for get stores")
def step_impl(context):
    stores = context.response.json()
    assert_that(stores, has_item("stores"))
    assert_that(stores["stores"], instance_of(list))

    for store in stores["stores"]:
        assert_that(len(store.keys()), equal_to(2))
        assert_that(store, has_key("name"))
        assert_that(store, has_key("items"))


@step("I add store")
def step_impl(context):
    test.add_store()

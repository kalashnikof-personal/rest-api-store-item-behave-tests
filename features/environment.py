from behave import fixture, use_fixture
from common import test


@fixture
def delete_all_stores(context):
    stores = test.get_all_stores()
    for store in stores["stores"]:
        test.delete_store(store["name"])


def before_all(context):
    test.log_separator()
    test.logger.debug("Setup.")
    use_fixture(delete_all_stores, context)


def after_all(context):
    test.log_separator()
    test.logger.debug("Tear-down.")


def before_scenario(context, scenario):
    test.log_separator()
    test.logger.debug(f"START: {scenario}")


def after_scenario(context, scenario):
    test.logger.debug(f"FINISH: {scenario} {scenario.status}")

import time

from behave import *


@given('I am on the Welcome page')
def step_impl(context):
    context.browser.driver.get("https://the-internet.herokuapp.com/")
    time.sleep(2)


@when('I click the Form Authentication button')
def step_impl(context):
    form_authentication = context.browser.get_form_authentication()
    form_authentication.click()
    time.sleep(2)


@then('I am redirected to the login page')
def step_impl(context):
    expected_url = "https://the-internet.herokuapp.com/login"
    assert context.browser.get_current_url() == expected_url


@when('I click the Typos button')
def step_impl(context):
    typos_link = context.browser.get_typos_url()
    typos_link.click()
    time.sleep(2)


@then('I am redirected to the Typos page')
def step_impl(context):
    expected_url = "https://the-internet.herokuapp.com/typos"
    assert context.browser.get_current_url() == expected_url


@when('I click the Inputs button')
def step_impl(context):
    inputs_link = context.browser.get_inputs_url()
    inputs_link.click()
    time.sleep(2)


@then('I am redirected to the Inputs page')
def step_impl(context):
    expected_url = "https://the-internet.herokuapp.com/inputs"
    assert context.browser.get_current_url() == expected_url





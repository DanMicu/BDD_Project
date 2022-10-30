from browser import Browser
from features.pages.signin_page import SignInPage
from features.pages.signup_page import SignUpPage


def before_all(context):
    print("Setting the browser!!")
    context.browser = Browser()
    context.signin_page = SignInPage(context.browser.driver)
    context.signup_page = SignUpPage(context.browser.driver)


def after_all(context):
    context.browser.close()

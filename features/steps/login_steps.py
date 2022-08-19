# contains steps to be used on the login page.
from features.pages import login
from behave import given

@given(u'I go to php travels')
def log_in(context):
    # TODO add login logic here
    print('test')
    # go to url and
    # enter email
    # enter passwrong
    # click on submit button
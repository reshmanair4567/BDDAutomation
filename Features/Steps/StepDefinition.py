from behave import *
from selenium.webdriver import Chrome

@given(u'User is on registration page')
def step_impl(context):
    context.driver.get("http://www.thetestingworld.com/registration")

@when(u'User enters name')
def step_impl(context):
    context.driver.find_element_by_name('jform[name]').send_keys("test1234")

@when(u'User enters username')
def step_impl(context):
    context.driver.find_element_by_name('jform[username]').send_keys('hello1234')


@when(u'User enters password')
def step_impl(context):
    context.driver.find_element_by_name('jform[password1]').send_keys('abcd')

@when(u'User enters Confirm Password')
def step_impl(context):
    context.driver.find_element_by_name('jform[password2]').send_keys('abcd')


@when(u'User enters email')
def step_impl(context):
    context.driver.find_element_by_name('jform[email1]').send_keys('abcd@abc.com')


@when(u'user enters confirm email address')
def step_impl(context):
    context.driver.find_element_by_name('jform[email2]').send_keys('abcd@abc.com')

@when(u'User clicks on Register button')
def step_impl(context):
    context.driver.find_element_by_xpath("//button[@type='submit' and @class='validate']").click()


@then(u'User should be registered successfully')
def step_impl(context):
    print("Registered")


@when(u'User enters duplicate username')
def step_impl(context):
    context.driver.find_element_by_name('jform[username]').send_keys('duplicate')

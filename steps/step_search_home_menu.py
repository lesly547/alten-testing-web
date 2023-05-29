from pages.home import HomePage
import os
import time
from behave import *
from selenium import webdriver

script_dir = os.path.dirname(os.path.realpath(__file__))
chromepath = os.path.join(script_dir, "drivers/chromedriver")
driver = webdriver.Chrome(executable_path=chromepath)


@given(u"user access to Alten website")
def user_access_to_alten_website(context):
    driver.get(HomePage.get_base_url())
    context.home_page = HomePage(driver)
    time.sleep(6)


@step(u"cookies accept")
def cookies_accept(context):
    if context.home_page.find_button_accept_cookies():
        context.home_page.get_button_accept_cookies().click()

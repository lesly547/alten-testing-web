from selenium.webdriver import Keys
from pages.search import SearchPage
from pages.home import HomePage
import os
import time
from behave import *
from selenium import webdriver

script_dir = os.path.dirname(os.path.realpath(__file__))
chromepath = os.path.join(script_dir, "drivers/chromedriver")


@given(u"user access to Alten website")
def user_access_to_alten_website(context):
    context.driver = webdriver.Chrome(executable_path=chromepath)
    context.driver.get(HomePage.get_base_url())
    context.home_page = HomePage(context.driver)
    context.driver.maximize_window()
    context.driver.save_screenshot("screenshots/user_access_to_alten_website.png")
    time.sleep(4)


@step(u"cookies accept")
def cookies_accept(context):
    if context.home_page.find_button_accept_cookies():
        context.driver.save_screenshot("screenshots/cookies_accept.png")
        context.home_page.get_button_accept_cookies().click()


@step(u"selects icon search")
def selects_icon_search(context):
    context.home_page.get_button_search().click()
    context.driver.save_screenshot("screenshots/selects_icon_search.png")


@when(u"searching {text_search}")
def searching_text_search(context, text_search):
    context.home_page.get_input_search().send_keys(text_search, Keys.ENTER)
    context.driver.save_screenshot("screenshots/searching_text_search.png")


@then(u"the page shows a list of results")
def the_page_shows_a_list_of_results(context):
    context.search_page = SearchPage(context.driver)
    context.search_page.get_list_search_page()
    context.driver.execute_script("window.scrollTo(0, 300)")
    context.driver.save_screenshot("screenshots/the_page_shows_a_list_of_results.png")


@step(u"select the second item")
def select_the_second_item(context):
    context.search_page.get_second_position_list_search().click()
    context.driver.execute_script("window.scrollTo(0, 300)")
    time.sleep(2)
    context.driver.save_screenshot("screenshots/select_the_second_item.png")
    context.driver.close()


@then(u"shows a message indicating the number of results")
def shows_a_message_indicating_the_number_of_results(context):
    context.search_page = SearchPage(context.driver)
    assert "0" in context.search_page.get_number_results().text
    time.sleep(2)
    context.driver.save_screenshot("screenshots/shows_a_message_indicating_the_number_of_results")
    context.driver.close()

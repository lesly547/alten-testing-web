from selenium.webdriver import Keys

from helpers.common import create_screenshots, save_results, save_csv
from pages.search import SearchPage
from pages.home import HomePage
import os
import time
import logging
from behave import *
from selenium import webdriver

script_dir = os.path.dirname(os.path.realpath(__file__))
chromepath = os.path.join(script_dir, "drivers/chromedriver")
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


@given(u"user access to Alten website")
def user_access_to_alten_website(context):
    try:
        logging.info('Start user access to Alten website')
        context.driver = webdriver.Chrome(executable_path=chromepath)
        context.driver.get(HomePage.get_base_url())
        context.home_page = HomePage(context.driver)
        context.driver.maximize_window()
        create_screenshots(context, "user_access_to_alten_website.png")
        time.sleep(4)
        logging.info('End user access to Alten website')
        save_results("user_access_to_alten_website", "Success", 'None')
    except Exception as e:
        save_results("user_access_to_alten_website", "Error", e)


@step(u"cookies accept")
def cookies_accept(context):
    try:
        logging.info('Start cookies accept')
        if context.home_page.find_button_accept_cookies():
            logging.info('Exist cookies accept button')
            create_screenshots(context, "cookies_accept.png")
            context.home_page.get_button_accept_cookies().click()
        else:
            logging.warning('Not exist cookies accept')
        save_results("cookies_accept", "Success", 'None')
    except Exception as e:
        save_results("cookies_accept", "Error", e)


@step(u"selects icon search")
def selects_icon_search(context):
    try:
        context.home_page.get_button_search().click()
        create_screenshots(context, "selects_icon_search.png")
        save_results("selects_icon_search", "Success", 'None')
    except Exception as e:
        save_results("selects_icon_search", "Error", e)


@when(u"searching {text_search}")
def searching_text_search(context, text_search):
    try:
        context.home_page.get_input_search().send_keys(text_search, Keys.ENTER)
        create_screenshots(context, "searching_text_search.png")
        save_results("searching_text_search", "Success", 'None')
    except Exception as e:
        save_results("searching_text_search", "Error", e)


@then(u"the page shows a list of results")
def the_page_shows_a_list_of_results(context):
    try:
        context.search_page = SearchPage(context.driver)
        context.search_page.get_list_search_page()
        context.driver.execute_script("window.scrollTo(0, 300)")
        create_screenshots(context, "the_page_shows_a_list_of_results.png")
        save_results("the_page_shows_a_list_of_results", "Success", 'None')
    except Exception as e:
        save_results("the_page_shows_a_list_of_results", "Error", e)


@step(u"select the second item")
def select_the_second_item(context):
    try:
        context.search_page.get_second_position_list_search().click()
        context.driver.execute_script("window.scrollTo(0, 300)")
        time.sleep(2)
        create_screenshots(context, "select_the_second_item.png")
        save_csv('Selecting_a_search_result_by_keyword.csv')
        context.driver.close()
        save_results("select_the_second_item", "Success", 'None')
    except Exception as e:
        save_results("select_the_second_item", "Error", e)


@then(u"shows a message indicating the number of results")
def shows_a_message_indicating_the_number_of_results(context):
    try:
        context.search_page = SearchPage(context.driver)
        assert "0" in context.search_page.get_number_results().text
        time.sleep(2)
        create_screenshots(context, "shows_a_message_indicating_the_number_of_results.png")
        save_csv('Validate_in_the_search_by_keyword_is_0.csv')
        context.driver.close()
        save_results("shows_a_message_indicating_the_number_of_results", "Success", '')
    except AssertionError as e:
        save_results("shows_a_message_indicating_the_number_of_results", "Error", e)

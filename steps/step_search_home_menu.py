from selenium.webdriver import Keys
from pages.search import SearchPage
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
    driver.maximize_window()
    driver.save_screenshot("screenshots/user_access_to_alten_website.png")
    time.sleep(4)


@step(u"cookies accept")
def cookies_accept(context):
    if context.home_page.find_button_accept_cookies():
        driver.save_screenshot("screenshots/cookies_accept.png")
        context.home_page.get_button_accept_cookies().click()


@step(u"selects icon search")
def selects_icon_search(context):
    context.home_page.get_button_search().click()
    driver.save_screenshot("screenshots/selects_icon_search.png")
    time.sleep(3)


@when(u"searching {text_search}")
def searching_text_search(context, text_search):
    context.home_page.get_input_search().send_keys(text_search, Keys.ENTER)
    driver.save_screenshot("screenshots/searching_text_search.png")
    time.sleep(3)


@then(u"the page shows a list of results")
def the_page_shows_a_list_of_results(context):
    context.search_page = SearchPage(driver)
    context.search_page.get_list_search_page()
    driver.execute_script("window.scrollTo(0, 300)")
    driver.save_screenshot("screenshots/the_page_shows_a_list_of_results.png")
    time.sleep(3)


@step(u"select the second item")
def select_the_second_item(context):
    context.search_page.get_second_position_list_search().click()
    time.sleep(3)
    driver.execute_script("window.scrollTo(0, 300)")
    driver.save_screenshot("screenshots/select_the_second_item.png")
    driver.close()

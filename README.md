# Alten-testing-web

This repository contains automated tests for the Alten website. It uses Selenium and Python to execute user interface tests.

## Requirements

Make sure you have the following requirements before running the tests:

- This code makes use of Python, you can download [Here](https://www.python.org/downloads/). 
- This code makes use of Selenium Framework, you can download [Here](https://www.selenium.dev/downloads/).

## Setup

Follow these steps to set up the environment:

1. Clone the repository:

```shell
git clone https://github.com/lesly547/alten-testing-web.git
```

2. Navigate to the repository directory:

```shell
cd alten-testing-web
```

3. Install the dependencies:

```shell
pip install -r requirements.txt
```

4. Execute tests

```shell
behave
```

## Project Structure

```
.
├── drivers
│   └──  chromedriver.exe
├── features
│   └── search-home-menu.feature
├── helpers
│   └── common.py
├── pages
│   ├── home.py
│   └── search.py
├── reports
│   ├── Selecting_a_search_result_by_keyword.csv
│   └── Validate_in_the_search_by_keyword_is_0.csv
├── screenshots
│   ├── cookies_accept.png
│   ├── searching_text_search.png
│   ├── select_the_second_item.png
│   ├── selects_icon_search.png
│   ├── shows_a_message_indicating_the_number_of_results.png
│   ├── the_page_shows_a_list_of_results.png
│   └── user_access_to_alten_website.png
├── steps
│   └── step_search_home_menu.py
├── requirements
└── README.md
```
### Drivers
This repository contains the folder where to place the drivers. If you already have it downloaded, put it in the corresponding folder. If you want any other you can download it below


  * Chromedriver 
 [Here](https://chromedriver.chromium.org/downloads)

  * Geckodriver
  [Here](https://github.com/mozilla/geckodriver/releases)

### Features
Is the folder where the features are stored.

### Helpers
Is the folder where files with reusable functions are stored. 

### Pages
Is the folder where files with the locators of each page are stored.

### Reports
Is the folder where files with test execution reports for each scenario are stored.

### Screenshots
Is the folder where the screenshots of each test step are stored.

### Steps
Is the folder where the function files of each step are stored.
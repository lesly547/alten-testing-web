Feature: Search home menu
  Scenario: Selecting a search result by keyword
    Given user access to Alten website
    And cookies accept
    And selects icon search
    When searching expoQA
    Then the page shows a list of results
    And select the second item


  Scenario: Validate in the search by keyword is 0
    Given user access to Alten website
    And cookies accept
    And selects icon search
    When searching aaa
    Then shows a message indicating the number of results
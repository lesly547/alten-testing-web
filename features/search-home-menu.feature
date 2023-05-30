Feature: Search home menu
  Scenario: User searches in input search home page
    Given user access to Alten website
    And cookies accept
    And selects icon search
    When searching expoQA
    Then the page shows a list of results
    And select the second item
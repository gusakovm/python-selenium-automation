# Created by Max Gusakov
Feature: Help might be found in sandwich menu and the search shows relevant result

  Scenario: Help-center item appears in sandwich menu
    Given Open Amazon page
    When Open sandwich menu
    And Scroll down sandwich menu
    Then Help item is visible in sandwich menu

  Scenario: Help-center item in sandwich menu shows expected page
    Given Open Amazon page
    When Open sandwich menu
    And Scroll down sandwich menu
    And Click to the Help item in the menu list
    Then The page AmazonHelpCenter is shown

  Scenario: Help-center search shows relevant result in the title
    Given Open AmazonHelpCenter page
    When Input cancel order to the search field
    And Click on search button
    Then Search block shows Cancel Items or Orders in the title

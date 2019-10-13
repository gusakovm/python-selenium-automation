# Created by Max Gusakov
Feature: Shopping Cart works well

  Scenario: Empty shopping cart is empty at Amazon starts
    Given Open Amazon page
    When Click to Shopping Cart button
    Then The page AmazonCart is shown
    And Amazon Cart page title is Cart is empty
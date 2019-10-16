# Created by Max Gusakov
Feature: Shopping Cart works well

  Scenario: Empty shopping cart is empty at Amazon starts
    Given Open Amazon page
    When Click to Shopping Cart button
    Then The page AmazonCart is shown
    And Amazon Cart page title is Cart is empty

  Scenario: Add any item into the cart and check it's there
    Given Open Amazon page
    When Search Amazon Kindle product
    And Add 0 index product to the cart
    Then Make sure the cart isn't empty (by counter)
    And Make sure the item shows at the Cart page
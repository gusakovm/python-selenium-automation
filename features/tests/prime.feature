# Created by mbprm at 16.10.2019
Feature: Some test for Amazon Prime page

  Scenario: Amazon Prime has expected number of info-boxes
    Given Open AmazonPrime page
    Then There are 8 info-boxes on the page

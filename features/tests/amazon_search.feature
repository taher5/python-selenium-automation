# Created by Svetlana at 4/4/19
Feature: Test Scenarios for Search functionality

  Scenario: User can search for a product
    Given Open Amazon page
    When Input DRESS into Amazon search field
    And Click on Amazon search icon
    Then Product results for DRESS are shown on Amazon
    And First result contains DRESS


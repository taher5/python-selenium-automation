# Created by Svetlana at 4/4/19
Feature: Test Scenarios for Search functionality

  Scenario: Logged out user sees Sign in page when clicking Orders
    Given Open Amazon page
    When Click Orders
    Then Verify Sign in page opened

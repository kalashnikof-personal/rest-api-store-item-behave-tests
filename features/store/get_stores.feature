Feature: API to get list of stores
  As a user, I want to get list of stores.

  Background: Add two stores.
    Given I add store
    And I add store

  Scenario: Get list of stores
    When I set request url 'stores'
    And I set request method 'get'
    And I send request
    Then I get response code '200'
    And I get correct response body for get stores

@fixture.delete_all_stores
Feature: API to add a new store to list of stores
  As a user, I want to add a new store to my list of stores.

  Scenario: Add new store
    When I set request url 'store'
    And I set request method 'post'
    And I set store name
    And I send request
    Then I get response code '201'
    And I get correct response body for add store
    And I get store in list of stores

  Scenario: Add new store with same name
    When I set request url 'store'
    And I set request method 'post'
    And I set store name
    And I send request
    And I send request
    Then I get response code '400'
    And I get correct store already exists message

# language: en
@gametest
Feature: GameTest

  Scenario: Making a request
    When I call the "GetProjectList" API
    Then the value at "Projects" should be a list

  Scenario: Handling errors
    When I attempt to call the "GetProjectInfo" API with:
    | id | 2e534be2-9d45-46f2-9915-56ba9ff83be5 |
    Then I expect the response error code to be "NotFound"
    And I expect the response error to contain a message

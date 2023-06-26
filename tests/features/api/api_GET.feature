Feature: Test CRUD operations with Sample APIs

  Scenario: GET Books API
    Given I am a sample GET API
    When I set header param request content type as "application/json"
    And I set "GET" method and send the request
    Then I receive valid HTTP response code "200" for "GET" and expect response body is non-empty

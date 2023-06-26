Feature: Test CRUD operations with Sample APIs

  Scenario Outline: DELETE Books API
    Given I am a sample DELETE API
    When I set header param request content type as "application/json"
    And I set "GET" method and send the request
    And I set "POST" method and send the request to get Auth token
    And I send "DELETE" HTTP request to delete a record
    Then I set "GET" method and send the request
    And I receive valid HTTP response code "200" for "DELETE" and expect response body is non-empty

    Examples:
      | payload                                      |
      | {"title": "POST API", "author": "Saad", "type": "python", "dateAdded": "Sun May 14 01:00:00 PKT 2023"} |
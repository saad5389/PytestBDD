Feature: Test CRUD operations with Sample APIs

  Scenario Outline: PUT Books API
    Given I am a sample PUT API
    When I set header param request content type as "application/json"
    And I set "GET" method and send the request
    And I send "PUT" HTTP request with "<payload>"
    Then I set "GET" method and send the request
    And I receive valid HTTP response code "200" for "PUT" and expect response body is non-empty


    Examples:
      | payload                                          |
      | {"title": "API", "author": "Saad1", "type": "put", "dateAdded": "Tue May 16 10:55:00 PKT 2023"} |

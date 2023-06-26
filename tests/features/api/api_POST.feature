Feature: Test CRUD operations with Sample APIs

  Scenario Outline: POST Books API
    Given I am a sample POST API
    When I set header param request content type as "application/json"
    And I set "POST" method and send the request with "<payload>"
    Then I set "GET" method and send the request
    And I receive valid HTTP response code "201" for "POST"

    Examples:
      | payload                                      |
      | {"title": "POST API", "author": "Saad5389", "type": "python", "dateAdded": "Sun May 14 01:00:00 PKT 2023"} |
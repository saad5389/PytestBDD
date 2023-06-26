Feature: Open Amwell website
  and user should not login with invalid creds and validation messages appears

  Scenario Outline: login with invalid creds
    Given Login page
    When the user enter Code "<code>" and clicks on Next button
    And the user clicks on login button
    And the user enter email address "<email>" and password "<password>"
    And the user clicks on login button
    Then user should not login and validation message should appear

    Examples:
      | code      | email                 | password   |
      | rqaclinic | invalid_user@yopmail.com | Avizia20!9 |
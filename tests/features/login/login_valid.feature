Feature: Open Amwell website
  and user should login with valid creds successfully

  Scenario Outline: login with valid creds
    Given Login page
    When the user enter Code "<code>" and clicks on Next button
    And the user clicks on Login button
    And the user enter email address "<email>" and password "<password>"
    And the user clicks on login button
    Then user should login successfully and lands on dashboard with Welcome heading

    Examples:
      | code      | email                 | password   |
      | rqaclinic | rqa_admin@yopmail.com | Avizia20!9 |
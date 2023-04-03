Feature: Open Amwell website
  and user should not login with invalid creds and validation messages appears

  Scenario: login with invalid creds
    Given Login page
    When the user enter Code "testclinic" and clicks on Next button
    And the user clicks on login button
    And the user enter email address "preprod@mailinator.com"
    And the user enter password "Abc1234."
    And the user clicks on login button
    Then user should not login and validation message should appear

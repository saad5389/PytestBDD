Feature: Open Amwell website
  and user should login with valid creds successfully

  Scenario: login with valid creds
    Given Login page
    When the user enter Code "testclinic" and clicks on Next button
    And the user clicks on Login button
    And the user enter email address "preprodadmin@mailinator.com"
    And the user enter password "Abc1234-"
    And the user clicks on login button
    Then user should login successfully and lands on dashboard with Welcome heading

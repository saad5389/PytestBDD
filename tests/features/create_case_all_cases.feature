Feature: Login with valid creds and user should create a case without Patient from all cases successfully

  Scenario: login with valid creds and create case from all cases without Patient
    Given Login and create a case
    When user enter code "testclinic" and login successfully with valid creds "preprodadmin@mailinator.com", "Abc1234-"
    And user go through case creation steps from all cases
    Then case created successfully without Patient

Feature: Login with valid creds and user should create a case without Patient from all cases successfully

  Scenario: Create case from all cases without Patient
    Given Login page
    When user enter code "intauto" and login successfully with valid creds "blackwell-testing@amwell.com", "7K+RutL%Tu$9SacD"
    And user go through case creation steps from all cases
    Then case created successfully without Patient
    And search the created case on All cases page

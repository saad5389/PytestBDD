Feature: Login with valid creds and user should create a case with Patient

  Scenario: Create case with Patient
    Given Login page
    When user enter code "intauto" and login successfully with valid creds "blackwell-testing@amwell.com", "7K+RutL%Tu$9SacD"
    And user search for a patient firstname "Ajay" and lastname "Kumar"
    And user go through case creation steps from all cases
    Then user creates a case successfully with patient

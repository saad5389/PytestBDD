Feature: Login with valid creds and user should create a case with Patient

  Scenario: Add new Patient
    Given Login page
    When user enter code "intauto" and login successfully with valid creds "blackwell-testing@amwell.com", "7K+RutL%Tu$9SacD"
    And user clicks on Add patient and enter mandatory fields firstname, lastname, "2000-01-01" and "Male"
    Then new patient created successfully
    And verify new patient on patient-search page
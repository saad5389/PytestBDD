Feature: User should create a case and assign to me, it should appear in my cases tab

  Scenario Outline: Assign case appears in My Cases tab
    Given Login page
    When user enter code "<code>" and login successfully with valid creds "<email>", "<password>"
    And user go through case creation steps from all cases
    Then case created successfully and assigned to me
    And search the created case on my cases page

    Examples:
      | code      | email                 | password   |
      | rqaclinic | rqa_admin@yopmail.com | Avizia20!9 |
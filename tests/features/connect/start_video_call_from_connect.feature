Feature: User should successfully join the call from Connect module

  Scenario Outline: Start video call from Connect
    Given Login page
    When user enter code "<code>" and login successfully with valid creds "<email>", "<password>"
    And user go to Quick Connect and create a room with "<email>" address
    Then user join the newly created room
    And user ends the call

    Examples:
      | code      | email                 | password   |
      | rqaclinic | rqa_admin@yopmail.com | Avizia20!9 |
Feature: Open Amwell website
  and request signup with new user successfully

  Scenario: Request signup with new user
    Given Code page
    When the user enter Code "intauto" and clicks on Next button
    And the user clicks on Sign Up button
    And the user enter Firstname "first", Lastname "last" and Email
    Then the user clicks on Request Access button should Signup successfully and lands on Request Sent screen with Thankyou message
    And user login with admin user email "blackwell-testing@amwell.com" and password "7K+RutL%Tu$9SacD"
    And admin verify the signup request


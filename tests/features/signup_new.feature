Feature: Open Amwell website
  and signup with new user successfully

  Scenario: Signup with new user
    Given Code page
    When the user enter Code "testclinic" and clicks on Next button
    And the user clicks on Sign Up button
    And the user enter Firstname "first", Lastname "last" and Email "preprodprovider@mailinator.com"
    Then the user clicks on Request Access button should Signup successfully and lands on Request Sent screen with Thankyou message

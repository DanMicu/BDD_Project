Feature: Test 3

  Scenario: Sign-up to jules.app
    Given We have the jules webpage loaded
    When We click sign up
    And We click the Personal button
    And we click continue
    And We input a correct first name
    And We click continue
    And we input a correct last name
    And We click continue
    And We input a wrong email
    Then The Please enter a valid email address error is displayed
    And We clear the email input
    And We input a correct email
    And The error message is no longer displayed




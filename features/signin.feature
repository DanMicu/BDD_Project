Feature: Test 1

  Scenario: Sign-In attempt with correct email and no password
    Given We are on the Sign-In page
    When We enter the correct email
    And We leave the password empty
    Then Log In button is disabled
    And  The Please enter your password error is present


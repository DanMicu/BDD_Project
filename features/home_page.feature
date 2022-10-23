Feature: Home Page

  Scenario: Redirect to Form Authentication
    Given I am on the Welcome page
    When I click the Form Authentication button
    Then I am redirected to the login page

  Scenario: Redirect to Typos
    Given I am on the Welcome page
    When I click the Typos button
    Then I am redirected to the Typos page

  Scenario: Redirect to Inputs
    Given I am on the Welcome page
    When I click the Inputs button
    Then I am redirected to the Inputs page


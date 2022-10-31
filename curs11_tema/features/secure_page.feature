Feature: Secure Page

  Scenario: Logout
    Given I am on the login page
    And  I enter the correct login credentials
    And I click login
    And I am on the Secure page
    When I click the logout button
    Then I am successfully logged out

  Scenario: You logged into a secure area!
    Given I am on the login page
    And  I enter the correct login credentials
    And I click login
    When I am redirected to the Secure page
    Then 'You logged into a secure area! is displayed






Feature: Login Page

  Scenario: Login attempt with valid credentials
    Given I am on the Login Page
    When I introduce the correct username
    And I introduce the correct password
    Then I click the login button
    And I am successfully logged in

  Scenario: Login attempt with both invalid credentials
    Given I am on the Login Page
    When I introduce a wrong username
    And I introduce a wrong password
    Then I click the login button
    And The 'Your username is invalid!' error appears

Feature:Verifying registration functionality
  @smoke
  Scenario:Registration with valid data
    Given User is on registration page
    When User enters name
    And User enters username
    And User enters password
    And User enters Confirm Password
    And User enters email
    And user enters confirm email address
    And User clicks on Register button
    Then User should be registered successfully

   @sanity @smoke
  Scenario:Registration with duplicate username data
    Given User is on registration page
    When User enters name
    And User enters duplicate username
    And User enters password
    And User enters Confirm Password
    And User enters email
    And user enters confirm email address
    And User clicks on Register button
    Then User should be registered successfully
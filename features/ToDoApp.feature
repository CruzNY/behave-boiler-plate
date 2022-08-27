Feature: Test to add item
 
Scenario: Test Advance boy
  Given I go to 4davanceboy to add item
  Then I Click on first checkbox and second checkbox
  When I enter item to add
  When I click add button
  Then I enter "Yey, Let's add it to list" in the "sampletodotext" field'
  Then I verify that the "element" is displayed



  
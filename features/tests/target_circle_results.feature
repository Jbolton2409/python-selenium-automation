Feature: Target Circle Test Cases


  Scenario: Verify Target Circle story cards
    Given Open Target circle page
    Then at least 2 story cards under Unlock added value are displayed


  Scenario: User can add product to cart
    Given Open Target main page
    When search for toothpaste
    And Click on Add to Cart Button
    And Confirm Add to Cart Button
    Then Verify cart has 1 item(s)




  Scenario: Verify Target Help UI
    Given Open Target main page
    Then Help search bar is visible

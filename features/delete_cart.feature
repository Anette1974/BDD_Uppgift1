
Feature: Töm hela varukorgen

Scenario:
Given Användaren har en eller flera böcker i varukorgen
When Användaren klickar på töm varukorg
Then Boken/ böckerna tas bort från varukorgen
And saldo i varukorgen uppdateras till 0
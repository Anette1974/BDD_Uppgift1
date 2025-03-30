@wip
Feature: Ta bort bok från varukorgen

Scenario:
Given Användaren har en eller flera böcker i varukorgen
When Användaren klickar på ta bort bok från varukorgen
Then Boken tas bort från varukorgen
And saldo i varukorgen uppdateras


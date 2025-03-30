@wip
Feature: Lägga till en bok i varukorgen

Scenario Outline:
  Given Användaren har en tom varukorg
  When Användaren klickar på "lägg till bok" för boken <book>
  Then Boken hamnar i varukorgen
  And summan i varukorgen ska uppdateras med priset för boken <price>

  Examples:
  | book           | price |
  | Kokbok         | 100   |
  | Gröna fingarar | 200   |
  | Koda själv     | 300   |
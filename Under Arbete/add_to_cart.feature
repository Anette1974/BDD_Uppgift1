@ok
Feature: Lägga till en bok i varukorgen

Scenario:
  Given Användaren har en tom varukorg
  When Användaren klickar på "lägg till bok"
  Then Boken hamnar i varukorgen
  And summan i varukorgen ska uppdateras med priset för boken
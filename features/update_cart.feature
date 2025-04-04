@ok
Feature: Öka antalet böcker om samma bok redan finns i varukorgen

Scenario:
Given Användaren vill beställa fler exemplar av bok som redan finns i varukorgen
When Användare klickar på "lägg till bok"
Then Antalet beställda böcker uppdateras i varukorgen

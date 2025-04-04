from behave import given, when, then

@given(u'Användaren vill beställa fler exemplar av bok som redan finns i varukorgen')
def step_current_cart(context):
    context.cart = "Syslöjd"
    context.count = 1
    print(f"Användaren har sedan tidigare {context.count} exemplar av boken {context.cart} i varukorgen")


@when(u'Användare klickar på "lägg till bok"')
def step_add_same_book_twice(context):
    assert context.count > 0, "Boken finns inte i varukorgen"
    context.count +=1
    print("Användaren klickar på lägg till bok.")


@then(u'Antalet beställda böcker uppdateras i varukorgen')
def step_impl(context):
    expected_count = 2
    assert context.count == expected_count, f"Förväntade {expected_count} exemplar, men fick {context.count} exemplar"
    print(f"Nu finns det {context.count} exemplar av boken {context.cart} i varukorgen")

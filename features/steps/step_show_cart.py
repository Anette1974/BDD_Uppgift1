from behave import given, when, then

@given(u'Användaren är på bokhandelns webshop')
def step_webshop(context):
    context.cart = ["Koda för nybörjare"]
    print("Användaren är bokhandelns webshop")


@when(u'Användaren klickar på ikon för varukorg')
def step_click_cart(context):
    print("Användaren klickade på varukorgen")


@then(u'Varukorgen visar aktuell köpesumma och antal böcker')
def step_show_cart(context):
    assert len(context.cart) > 0, "Varukorgen är tom"
    print(f"Varukorgen innehåller: {context.cart}")

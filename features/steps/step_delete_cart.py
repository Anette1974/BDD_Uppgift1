from behave import given, when, then

@given(u'Böcker i varukorgen')
def step_cart_not_empty(context):
    context.cart = ["Kokbok", "Snickra"]
    assert len(context.cart) > 0, "Varukorgen är tom"
    print(f"I varukorgen ligger följande böcker {context.cart}")


@when(u'Användaren klickar på töm varukorg')
def step_when_click_empty(context):
    context.button = True
    print("Töm varukorg knapp är tryckt")


@then(u'Boken/ böckerna tas bort från varukorgen')
def step_when_clean_cart(context):
    context.cart = []
    print("Varukorgen är tömd")


@then(u'saldo i varukorgen uppdateras till 0')
def step_impl(context):
    context.amount = 0
    print("Köpesumman är noll")


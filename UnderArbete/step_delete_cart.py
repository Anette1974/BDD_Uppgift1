from behave import given, when, then

@given(u'Användaren har en eller flera böcker i varukorgen')
def step_cart_not_empty(context, cart):
    context.cart = ["Bok 1"]
    raise NotImplementedError(u'STEP: Given Användaren har en eller flera böcker i varukorgen')


@when(u'Användaren klickar på töm varukorg')
def step_when_click_empty(context):
    context.button = True
    print("Töm varukorg knapp är tryckt")


@then(u'Boken/ böckerna tas bort från varukorgen')
def step_when_clean_cart(context, cart):
    context.cart = []
    print("Varukorgen är tömd")


@then(u'saldo i varukorgen uppdateras')
def step_impl(context, amount):
    context.amount = 0
    print("Köpesumman är noll")


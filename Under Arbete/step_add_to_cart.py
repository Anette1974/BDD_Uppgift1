from behave import given, when, then

@given(u'Användaren har en tom varukorg')
def step_given_book(context):
    context.cart = []
    context.book = "Gröna fingrar"


@when(u'Användaren klickar på "lägg till bok"')
def step_add_book(context):
    book = context.book
    context.cart.append(book)
    print("Användaren lägger till boken i varukorgen")


@then(u'Boken hamnar i varukorgen')
def step_cart_updated(context):
    print("Boken tillagd i varukorgen")


@then(u'summan i varukorgen ska uppdateras med priset för boken')
def step_amount_updated(context):
    print("Köpesumman uppdaterad")

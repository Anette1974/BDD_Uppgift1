from behave import given, when, then
'''
@given(u'Användaren har en eller flera böcker i varukorgen')
def step_actual_cart(context):
    context.cart = ["Gröna fingrar"]
    context.balance = 150
    print("Bok finns i varukorgen")'''


@when(u'Användaren klickar på ta bort bok från varukorgen')
def step_remove_from_cart(context):
    context.cart.remove("Gröna fingrar") # Tar bort boken från listan
    print("Boken har tagits bort")


@then(u'Boken tas bort från varukorgen')
def step_not_in_cart(context):
    assert "Gröna fingrar" not in context.cart, f"Gröna fingrar finns fortfarande i varukorgen: {context.cart}"
    print("Boken Gröna fingarar har tagits bort från varukorgen")

'''
@then(u'saldo i varukorgen uppdateras')
def step_balance_cart(context):
    context.balance -= 150
    print(f"Ny summa i varukorgen är: {context.balance} kr")'''

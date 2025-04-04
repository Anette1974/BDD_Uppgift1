@given(u'Användaren har en eller flera böcker i varukorgen')
def step_actual_cart(context):
    context.cart = ["Gröna fingrar"]
    context.balance = 150
    print("Bok finns i varukorgen")

@then(u'saldo i varukorgen uppdateras')
def step_balance_cart(context):
    context.balance -= 150
    print(f"Ny summa i varukorgen är: {context.balance} kr")
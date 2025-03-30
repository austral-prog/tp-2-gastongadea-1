def change():
    expense = 23.75
    money = 100
    print('Ingresar gasto:')
    print(expense)
    print('Dinero recibido')
    print(money)
    print()
    print('Vuelto')
    print()
    print('Pesos:')
    vuelto=money-expense
    print(vuelto)
    print('Centavos:')
    cents=int((vuelto-int(vuelto))*100)
    print(cents)

while True:
    primul_nr = input("Introdu primul numar: ")
    if primul_nr.isnumeric() is not True:
        while primul_nr.isnumeric() is not True:
            primul_nr = input("Introdu primul numar: ")
    al_doilea_nr = input("Introdu al doilea numarator: ")
    if al_doilea_nr.isnumeric() is not True:
        while al_doilea_nr.isnumeric() is not True:
            al_doilea_nr = input("Introdu al doilea numar: ")

    operatie = input("Alege operatie pe care doresti sa o executi: ")
    if operatie in ['+', '-', '*', '/']:
        if int(al_doilea_nr) == 0 and operatie == '/':
            print('Impartire la 0!!!')
            continue
        if operatie == '+':
            print(f"Suma numerelor {primul_nr} + {al_doilea_nr} = {int(primul_nr) + int(al_doilea_nr)}")
        elif operatie == '-':
            print(f"Diferenta numerelor {primul_nr} - {al_doilea_nr} = {int(primul_nr) - int(al_doilea_nr)}")
        elif operatie == '*':
            print(f"Produsul numerelor {primul_nr} * {al_doilea_nr} = {int(primul_nr) * int(al_doilea_nr)}")
        else:
            print(f"Catul impartirii numerelor {primul_nr} / {al_doilea_nr} = {int(primul_nr) / int(al_doilea_nr)}")
        break
    else:
        print(f"Alege o operatie: {','.join(['+', '-', '*', '/'])}")


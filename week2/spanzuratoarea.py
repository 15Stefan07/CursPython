cuvant = 'onomatopee'.lower()
cuvant_initial = list(cuvant)
"""o _ o _ _ _ o _ e e"""
"""literele sunt lowercase"""
"""avem 7 incercari"""

for index, value in enumerate(cuvant_initial):
    print(cuvant_initial[0], cuvant_initial[-1])
    if cuvant_initial[0] != value and cuvant_initial[-1] != value:
        cuvant_initial[index] = '_'

print(" ".join(cuvant_initial))
numar_incercari = 0
set_litere_incercate = set()

while numar_incercari <= 3:
    litera_incercata = input("Alege o litera: ").lower()
    if litera_incercata in cuvant_initial:
        print("Litera este deja afisata pe ecran!")
    elif litera_incercata in cuvant:
        for index, value in enumerate(cuvant):
            if litera_incercata == value:
                cuvant_initial[index] = litera_incercata
    else:

            if litera_incercata not in set_litere_incercate:
                numar_incercari += 1
            set_litere_incercate.add(litera_incercata)
            #print(set_litere_incercate)
            if numar_incercari == 3:
                print(f"Ai pierdut! Cuvantul initial era : {cuvant}")
                break
            print(f"Mai ai {3-numar_incercari} incercari.Ai incercat deja aceasta litera! Litere incercate sunt : {','.join(set_litere_incercate)}")
    if '_' not in cuvant_initial:
        print("Ai castigat!")
        break
    print(" ".join(cuvant_initial))
# print(litera_incercata)

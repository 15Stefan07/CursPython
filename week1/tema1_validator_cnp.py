cnp = input("Cititi un CNP: ")
while (cnp.isnumeric() is not True) or len(cnp) != 13:
    cnp = input("Cititi un CNP:")

# dummy_cnp = "5010715070070"
# print(dummy_cnp)
referinta = "279146358279"

S = cnp[0]
AA = cnp[1:3]
LL = cnp[3:5]
ZZ = cnp[5:7]
JJ = cnp[7:9]
NNN = cnp[9:12]
C = cnp[12]

C_ref = 0
suma = 0
an_nastere = ""
cifre_cnp = []
cifre_referinta = []
sir_nou = []

Persoana = {"Sex": "",
            "An": "",
            "Luna": "",
            "Zi": "",
            "Judet": "",
            "Numar": ""}

luni_an = {"01": "Ianuarie",
           "02": "Februarie",
           "03": "Martie",
           "04": "Aprilie",
           "05": "Mai",
           "06": "Iunie",
           "07": "Iulie",
           "08": "August",
           "09": "Septembrie",
           "10": "Octombrie",
           "11": "Noiembrie",
           "12": "Decembrie"}

judete = {"01": "Alba",
          "02": "Arad",
          "03": "Arges",
          "04": "Bacau",
          "05": "Bihor",
          "06": "Bistrita-Nasaud",
          "07": "Botosani",
          "08": "Brasov",
          "09": "Braila",
          "10": "Buzau",
          "11": "Caras-Severin",
          "12": "Cluj",
          "13": "Constanta",
          "14": "Covasna",
          "15": "Dambovita",
          "16": "Dolj",
          "17": "Galati",
          "18": "Gorj",
          "19": "Harghita",
          "20": "Hunedoara",
          "21": "Ialomita",
          "22": "Iasi",
          "23": "Ilfov",
          "24": "Maramures",
          "25": "Mehedinti",
          "26": "Mures",
          "27": "Neamt",
          "28": "Olt",
          "29": "Prahova",
          "30": "Satu Mare",
          "31": "Salaj",
          "32": "Sibiu",
          "33": "Suceava",
          "34": "Teleorman",
          "35": "Timis",
          "36": "Tulcea",
          "37": "Vaslui",
          "38": "Valcea",
          "39": "Vrancea",
          "40": "Bucuresti",
          "41": "Bucuresti sectorul 1",
          "42": "Bucuresti sectorul 2",
          "43": "Bucuresti sectorul 3",
          "44": "Bucuresti sectorul 4",
          "45": "Bucuresti sectorul 5",
          "46": "Bucuresti sectorul 6",
          "51": "Calarasi",
          "52": "Giurgiu"}

if int(S) == 1 or int(S) == 3 or int(S) == 5 or int(S) == 7:
    Persoana["Sex"] = "barbatesc"
elif int(S) == 2 or int(S) == 4 or int(S) == 6 or int(S) == 8:
    Persoana["Sex"] = "femeiesc"
elif int(S) == 9:
    Persoana["Sex"] = "persoana straina"

if int(S) == 1 or int(S) == 2:
    an_nastere = "19" + AA
elif int(S) == 3 or int(S) == 4:
    an_nastere = "18" + AA
elif int(S) == 5 or int(S) == 6:
    an_nastere = "20" + AA
elif int(S) == 7 or int(S) == 8:
    an_nastere = "persoana straina rezidenta in Romania"
elif int(S) == 9:
    an_nastere = "persoana straina"

Persoana["An"] = an_nastere
if luni_an.get(LL) is not None:
    Persoana["Luna"] = luni_an[LL]
Persoana["Zi"] = ZZ
if judete.get(JJ) is not None:
    Persoana["Judet"] = judete[JJ]
Persoana["Numar"] = NNN


for i in cnp[:12]:
    cifre_cnp.append(int(i))

for i in referinta:
    cifre_referinta.append(int(i))

for i, j in zip(cifre_cnp, cifre_referinta):
    sir_nou.append(i*j)

for i in sir_nou:
    suma += i

if suma % 11 == 10:
    C_ref = 1
else:
    C_ref = suma % 11



if int(S) == 0:
    print("CNP-ul este invalid!")
elif int(LL) > 12:
    print("CNP-ul este invalid!")
elif int(ZZ) > 31:
    print("CNP-ul este invalid!")
elif judete.get(JJ) is None:
    print("CNP-ul este invalid!")
elif int(NNN) == 0:
    print("CNP-ul este invalid!")
elif int(C) != C_ref:
    print("CNP-ul este invalid!")
else:
    print("CNP-ul este valid!")
    print("Datele persoanei: " + str(Persoana))

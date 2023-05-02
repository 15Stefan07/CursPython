class Clasa1:

    def __init__(self, marca, tip):
        self.marca = marca
        self.tip = tip

    def setare_culoare(self, culoare = "alb"):
        self.culoare = culoare

    def afisare_culoare(self):
        return self.culoare

    def __str__(self):
        return f"Masina marca {self.marca}, tip {self.tip}, culoarea {self.culoare}"


class Clasa2(Clasa1):

    def __init__(self, marca, tip):
        super().__init__(marca, tip)

    def incalzire_scaune(self,scaune_incalzite):
        self.scaune_incalzite = scaune_incalzite

    def __str__(self):
        if self.scaune_incalzite == "DA":
            return f"Masina marca {self.marca}, tip {self.tip}, culoarea {self.culoare} si cu scaune incalzite"
        else:
            return f"Masina marca {self.marca}, tip {self.tip}, culoarea {self.culoare} fara scaune incalzite"


class Clasa3(Clasa1):

    def __init__(self, marca, tip):
        super().__init__(marca,tip)


    def blocuri_led(self,Blocuri_Optice_LED):
        self.Blocuri_Optice_LED = Blocuri_Optice_LED

    def __str__(self):
        if self.Blocuri_Optice_LED == "DA":
            return f"Masina marca {self.marca}, tip {self.tip}, culoarea {self.culoare} cu blocuri optice led"
        else:
            return f"Masina marca {self.marca}, tip {self.tip}, culoarea {self.culoare} fara blocuri optice led"



masina_1 = Clasa2("ARO", "M461")
masina_1.incalzire_scaune("Nu")
masina_1.setare_culoare("rosu")

masina_2 = Clasa3("Dacia", "1310")
masina_2.blocuri_led("Nu")
masina_2.setare_culoare("negru")

print(masina_1.afisare_culoare())
print(masina_2.afisare_culoare())

print(masina_1)
print(masina_2)

masina_1.incalzire_scaune("DA")
print(masina_1)

masina_2.blocuri_led("DA")
print(masina_2)
class Catalog:

    def __init__(self, nume, prenume):
        self.nume = nume
        self.prenume = prenume
        self.materii = {}
        self.absente = 0

    def __str__(self):
        if self.absente == 1:
            return f"Studentul {self.nume} {self.prenume} are o absenta."
        else:
            return f"Studentul {self.nume} {self.prenume} are {self.absente} absente."


    def increment_absente(self):
        self.absente = self.absente + 1


    def sterge_n_absente(self, n):
        if n > self.absente:
            self.absente = 0
        else:
            self.absente = self.absente - n


class Extensie1(Catalog):
    def __init__(self, nume, prenume):
        super().__init__(nume, prenume)

    # def __str__(self):
    #     super().__str__()

    def adaugare_materie_note(self, denumire_materie="null", note=[]):
        self.materii[denumire_materie] = note

    def afisare_materii(self):
        lista_materii = []
        for x in self.materii:
            lista_materii.append(x)
        return f"Studentul {self.nume} {self.prenume} are materiile: {', '.join(lista_materii)}"

    def afisare_materii_si_medie(self):

        dictionar_nou = {}
        for x in self.materii:
            sum = 0
            contor = 0
            for y in self.materii[x]:
                if isinstance(y,int):
                    sum = sum + y
                    contor = contor + 1

            dictionar_nou[x] = sum / contor

        return f"Studentul {self.nume} {self.prenume} are materiile si mediile: {', '.join('{}: {}'.format(k, v) for k, v in dictionar_nou.items())}"



student_1 = Extensie1("Roata", "Ion")
# print(student_1)

student_1.increment_absente()
student_1.increment_absente()
student_1.increment_absente()
# print(student_1)

student_1.sterge_n_absente(2)
print(student_1)

student_2 = Extensie1("Cerc", "George")
# print(student_2)

student_2.increment_absente()
student_2.increment_absente()
student_2.increment_absente()
student_2.increment_absente()
# print(student_2)

student_2.sterge_n_absente(2)
print(student_2)


student_1.adaugare_materie_note("Python", [10, 9, 8])
student_2.adaugare_materie_note("Python", [5, 9, 6])

student_2.adaugare_materie_note("Matematica", [2, 5, 6])
student_1.adaugare_materie_note("Romana", [8, 6, 3])

print(student_1.afisare_materii())
print(student_2.afisare_materii())

print(student_1.afisare_materii_si_medie())
print(student_2.afisare_materii_si_medie())


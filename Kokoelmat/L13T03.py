
class auto():
    autonrekisterikilpi = ""
    autonmerkki = ""

    def __str__(self):
        return self.autonrekisterikilpi + " I " + self.autonmerkki

    def __init__ (self,autonrekisterikilpi="", autonmerkki=""):
        self.autonrekisterikilpi = autonrekisterikilpi
        self.autonmerkki = autonmerkki



muistio = []

for i in range(10):
    autorek = input("Auton rekisterikilpi?:")
    automer = input("Auton merkki?:")
    luku = auto(autorek, automer)
   
    muistio.append(luku)


muistio.sort(key=lambda car:car.autonrekisterikilpi)
for car in muistio:
    print(car)

print("-----------------------")

muistio.sort(key=lambda car:car.autonmerkki)
for car in muistio:
    print(car.autonrekisterikilpi, "-", car.autonmerkki)
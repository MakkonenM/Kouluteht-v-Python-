def print_info():
    print("I'm utils.info")


def sum(number1, number2):
    erotus = number1 - number2
    return erotus

def keskiarvo(number3, number4, number5):
    summa = number3 + number4 + number5
    ka = summa/3.0

    return ka

def auto_matka():
 # auton kulutus litraa/100km
 polttoaine = input("Kerro auton kulutus litraa/100km :")
 polttoaine = float(polttoaine)

 # kuljettu matka kilometreinä.
 matka = input("kuljettu matka kilometreinä:")
 matka = float(matka)

 # polttoaineen hinta euroa per litra
 hinta = input("polttoaineen hinta euroa per litra:")
 hinta = float(hinta)

 # Laskelmat
 bensan_kulutus = matka / 100 * polttoaine
 kulutus = hinta * bensan_kulutus


 print("-----------------------------------------")
 print("Polttoainetta kulunut: ", bensan_kulutus," litraa")
 print("Ajomatkan kulut:", kulutus, "€")
 print("==========================================")

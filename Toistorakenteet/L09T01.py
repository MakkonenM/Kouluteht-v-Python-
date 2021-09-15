
number = []

for pisteet in range(7):
    pisteet = int(input("Kirjoita viikon kunkin päivän sademäärä tähän ==> "))
    number.append(pisteet)
print("_______________________________________________________")
print("Viikon sademäärä ==>", sum(number))
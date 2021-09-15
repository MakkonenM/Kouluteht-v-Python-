oppilaat = []

while True:
    oppilas = input("Kirjoita oppilaiden nimet: ")
    if oppilas:
        oppilaat.append(oppilas)
    else:
        break

print("--------------------------------------------------------")

for oppilas in oppilaat:
    print(oppilas, end=", ")

oppilaat = len(oppilaat)
print("Kirjoitettujen opiskelijoiden määrä:", oppilaat)

rekisteri = []


print("Ohjelma lopetetaan tyhjällä syötteellä...")
print("___________________________________________")

while True:
    numero = input("Kirjoita Rekisterinumerot tähän: ")
    if numero:
        rekisteri.append(numero)
        rekisteri.sort()
    else:
        break

print("-----------------------------------------")

for numero in rekisteri:
    print(numero)
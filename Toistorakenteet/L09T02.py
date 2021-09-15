
number = []
while True:
    luku = int(input("Kirjoita luvut mitkä haluat laskee yhteen. (0 = pysäyttää toiminnan): "))
    if luku == 0:
        break
    number.append(luku)
print("Lukujen summa:", sum(number))

for luku in number:
    print("Luku", luku, "on listassa", number.count(luku), "kertaa.")

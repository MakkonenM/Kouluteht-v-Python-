number = []

while True:
    luku = input("Kirjoita kurssin arvosana tähän: ")
    if luku:
        number.append(luku)
    else:
        break

for luku in number:
        print("Luku", luku, "on listassa", number.count(luku), "kertaa.")


avg = sum(luku) / lenluku)


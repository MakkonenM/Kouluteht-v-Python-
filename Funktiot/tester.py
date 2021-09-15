from utils import print_info
from utils import sum
from utils import keskiarvo



print("Tuodaan funktio toisesta tiedostosta ")
print_info()

number1 = 12
number2 = 24
result = sum(number1, number2)
print("Tämän kahden luvun erotus ", result)


number3 = 30
number4 = 50
number5 = 20
result = keskiarvo(number3, number4, number5)
print("keskiarvo ", result)
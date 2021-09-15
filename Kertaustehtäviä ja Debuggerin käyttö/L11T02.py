
user_input = input("Fahrenheitit => Celsius = c tai Celsius => Fahrenheit = f: ")

if user_input == "c":
    rivi = input("Anna lampotila fahrenheit-asteina: ")
    fahrenheit = float(rivi)
    celsius = (fahrenheit - 32) * 5.0 / 9.0
    print(fahrenheit, "F on", celsius, "C")

elif user_input == "f":
    rivi1 = input("Anna lämpötila celsius-asteina: ")
    celsius1 = float(rivi1)
    fahrenheit1 = (celsius1 * 9/5) + 32    
    print(celsius1, "C on", fahrenheit1, "F")
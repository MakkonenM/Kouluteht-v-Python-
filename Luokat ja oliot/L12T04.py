import random
class Car1:
    Brand = ""
    Model = ""

    def show_info(self):
        msg = "1. Auton nimi ==>" + " " + self.Brand + " Auton malli  ==>" + " " + self.Model 
        return msg

auto1 = Car1()
auto1.Brand = "Skoda"
auto1.Model = "Octavia"
price1 = round(random.uniform(1000, 10000))


class Car2:
    Brand = ""
    Model = ""

    def show_info(self):
        msg = "2. Auton nimi ==>" + " " + self.Brand + " Auton malli  ==>" + " " + self.Model 
        return msg

auto2 = Car2()
auto2.Brand = "Audi"
auto2.Model = "A4"
price2 = round(random.uniform(1000, 10000))


class Car3:
    Brand = ""
    Model = ""

    def show_info(self):
        msg = "3. Auton nimi ==>" + " " + self.Brand + " Auton malli  ==>" + " " + self.Model 
        return msg

auto3 = Car3()
auto3.Brand = "Volvo"
auto3.Model = "V70"
price3 = round(random.uniform(1000, 10000))


class Car4:
    Brand = ""
    Model = ""

    def show_info(self):
        msg = "4. Auton nimi ==>" + " " + self.Brand + " Auton malli  ==>" + " " + self.Model 
        return msg

auto4 = Car4()
auto4.Brand = "BMW"
auto4.Model = "330D"
price4 = round(random.uniform(1000, 10000))


class Car5:
    Brand = ""
    Model = ""

    def show_info(self):
        msg = "4. Auton nimi ==>" + " " + self.Brand + " Auton malli  ==>" + " " + self.Model 
        return msg

auto5 = Car5()
auto5.Brand = "VW"
auto5.Model = "Golf IV"
price5 = round(random.uniform(1000, 10000))


print(auto1.show_info())
print(auto2.show_info())
print(auto3.show_info())
print(auto4.show_info())
print(auto5.show_info())
print("----------------------------")
print("Skoda:n hinta", price1,"€")
print("Audi:n inta", price2,"€")
print("Volvo:n hinta", price3,"€")
print("BMW:n hinta", price4,"€")
print("VM:n hinta", price5,"€")
print("----------------------------")
print("Autojen yhteishinta", price1 + price2 + price3 + price4 + price5, "€" )
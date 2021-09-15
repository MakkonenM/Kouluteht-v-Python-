class Car1:
    Brand = ""
    Model = ""
    Price = ""

    def show_info(self):
        msg = "1. Auton nimi ==>" + " " + self.Brand + " Auton malli  ==>" + " " + self.Model + " Auton hinta ==>" + " " + self.Price + "€"
        return msg

auto1 = Car1()
auto1.Brand = "Skoda"
auto1.Model = "Octavia"
auto1.Price = "3000"
auto1.price = 3000


class Car2:
    Brand = ""
    Model = ""
    Price = ""

    def show_info(self):
        msg = "2. Auton nimi ==>" + " " + self.Brand + " Auton malli  ==>" + " " + self.Model + " Auton hinta ==>" + " " + self.Price + "€"
        return msg

auto2 = Car2()
auto2.Brand = "Audi"
auto2.Model = "A4"
auto2.Price = "4000"
auto2.price = 4000


class Car3:
    Brand = ""
    Model = ""
    Price = ""

    def show_info(self):
        msg = "3. Auton nimi ==>" + " " + self.Brand + " Auton malli  ==>" + " " + self.Model + " Auton hinta ==>" + " " + self.Price + "€" 
        return msg

auto3 = Car3()
auto3.Brand = "Volvo"
auto3.Model = "V70"
auto3.Price = "5000"
auto3.price = 5000


print(auto1.show_info())
print(auto2.show_info())
print(auto3.show_info())
print("Autojen yhteishinta:", auto1.price + auto2.price + auto3.price)

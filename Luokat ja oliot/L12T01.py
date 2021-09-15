class Human:
    Name = ""
    Age = "" 

    def show_info(self):
        msg = "Nimesi ==>" + " " + self.Name + " Ikäsi ==>" + " " + self.Age
        return msg

Ihminen = Human()
Ihminen.Name = "Mikael Makkonen"
Ihminen.Age = "17"

print(Ihminen.show_info())

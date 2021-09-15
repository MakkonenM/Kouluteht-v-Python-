class Cat1:
    Name = ""
    Color = ""

    def show_info(self):
        msg =  "1. Kissan nimi ==>" + " " + self.Name + " Kissan väri ==>" + " " + self.Color + " *meow* "
        return msg

kissa1 = Cat1()
kissa1.Name = "Coco" 
kissa1.Color = "Harmaa"


class Cat2:
    Name = ""
    Color = ""

    def show_info(self):
        msg = "2. Kissan nimi ==>" + " " + self.Name + " Kissan väri ==>" + " " + self.Color + " *meow* "
        return msg

kissa2 = Cat2()
kissa2.Name = "Dodo" 
kissa2.Color = "Ruskea"

print(kissa1.show_info())
print(kissa2.show_info())

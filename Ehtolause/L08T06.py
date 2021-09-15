
vuosi = int(input("Vuosiluku: "))


if (vuosi % 4) == 0:
   if (vuosi % 100) == 0:
       if (vuosi % 400) == 0:
           print(vuosi, " on karkausvuosi")
       else:
           print(vuosi, " ei ole karkausvuosi")
   else:
       print(vuosi, " on karkausvuosi")
else:
   print(vuosi, " ei ole karkausvuosi")


<<<<<<< HEAD

	
=======
>>>>>>> fd05dcc0c1a52d3cdb6987b6cf87ab962eec0852

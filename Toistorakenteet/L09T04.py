# Tee ohjelma, joka kysyy käyttäjältä käyttäjän etu ja sukunimen.
# Tulosta käyttäjän etunimen ensimmäistä kirjainta niin monta kertaa kun etunimessä on kirjaimia. 
# sukunimi käänteisessä järjestyksessä. Siis esimerkiksi jos käyttäjä antaa etunimekseen 'Kirsi' ja sukunimeksi 'Kernell' tuloste olisi:
#'KKKKK'
#'llenreK'

nimi1 = input("Anna etunimesi: ") 
nimi2 = input("Anna sukunimesi: ") 


sanat = len(nimi1.split())
first = nimi1[0*sanat]
print(first)



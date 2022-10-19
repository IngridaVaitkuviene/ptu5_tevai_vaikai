# ASMENYS, SĄSKAITOS, BANKAI
# Padaryti programą, kurį leistų įvesti asmenis, bankus, asmenims priskirti 
# sąskaitas bankuose.

#     Asmuo turi vardą, pavardę, asmens kodą, tel. numerį.
#     Bankas turi pavadinimą, adresą, banko kodą, SWIFT kodą
#     Sąskaita turi numerį, balansą, priskirtą asmenį ir banką
#     Asmuo gali turėti daug sąskaitų tame pačiame arba skirtinguose bankuose

#     Padaryti duomenų bazės schemą.
#     Sukurti programą su UI konsolėje, kuri leistų: 
# įvesti asmenis, bankus, sąskaitas.
# Leistų vartotojui peržiūrėti savo sąskaitas ir jų informaciją, pridėti arba nuimti iš jų pinigų. 
# Taip pat leistų bendrai peržiūrėti visus bankus, vartotojus, sąskaitas ir jų informaciją.

from sqlalchemy.orm import sessionmaker
from _1019_asm_sask_bankai_model import engine, Asmuo, Bankas, Saskaita

session = sessionmaker(engine)()

def ivesti_asmeni():
    vardas = input("Įveskite vardą: ")
    pavarde = input("Įveskite pavardę: ")
    asm_kodas = int(input("Įveskite asmens kodą: "))
    mobilus = int(input("Įveskite mobilaus tel. nr.: "))
    asmuo = Asmuo(vardas=vardas, pavarde=pavarde, asm_kodas=asm_kodas, mobilus=mobilus)
    session.add(asmuo)
    session.commit()
    return asmuo

def ivesti_banka():
    pavadinimas = input("Įveskite pavadinimą: ")
    adresas = input("Įveskite adresą: ")
    b_kodas = int(input("Įveskite banko kodą: "))
    swift = input("Įveskite SWIFT kodą: ")
    bankas = Bankas(pavadinimas=pavadinimas, adresas=adresas, b_kodas=b_kodas, swift=swift)
    session.add(bankas)
    session.commit()
    return bankas

def ivesti_saskaita():
    numeris = int(input("Įveskite numerį: "))
    balansas = 0


def ivesti_pajamas_islaidas():
    pass

def perziureti_asmenis():
    pass

def perziureti_bankus():
    pass

def perziureti_saskaitas():
    pass

if __name__ == "__main__":
    while True:
        print("___Asmenų, bankų, sąskaitų duomenų bazė___")
        print("Programos meniu: ")
        print("0 - išeiti iš programos")
        print("1 - įvesti asmenį")
        print("2 - įvesti banką")
        print("3 - įvesti sąskaitą")
        print("4 - įvesti pajamas/išlaidas")
        print("5 - peržiūrėti asmenis")
        print("6 - peržiūrėti bankus")
        print("7 - peržiūrėti sąskaitas")
        try:
            pasirinkimas = int(input("Pasirinkite: "))
            if pasirinkimas == 0:
                print("Išėjote iš programos.")
                break
            elif pasirinkimas == 1:
                ivesti_asmeni()
            elif pasirinkimas == 2:
                ivesti_banka()
            elif pasirinkimas == 3:
                ivesti_saskaita()
            elif pasirinkimas == 4:
                ivesti_pajamas_islaidas()
            elif pasirinkimas == 5:
                perziureti_asmenis()
            elif pasirinkimas == 6:
                perziureti_bankus()
            elif pasirinkimas == 7:
                perziureti_saskaitas()
        except ValueError:
            print("!!!!!!!! KLAIDA: nurodykite skaičių 0-7 !!!!!!!!")
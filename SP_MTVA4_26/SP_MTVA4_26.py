import os
import random
import math

# leidsin lahenduse, et peale igat harjutust tuleb puhas leht https://stackoverflow.com/a/684344
def clear():
    os.system('cls')

# Ülesanne 1
print("Ülesanne 1")

print("Tere maailm!") 
nimi = input("Mis on sinu nimi? ")
print(f"Tere maailm! Tervitan sind, {nimi}!")
vanus = input("Mis on sinu vanus? ")
print(f"Tere maailm! Tervitan sind, {nimi}! Sa oled {vanus} aastat vana.")

input("Vajuta Enterit, et vaadata ülesannet 2.")

clear()

# Ülesanne 2
print("Ülesanne 2")

print("a. vanus = 18 on integral ehk int")
print("b. eesnimi = 'Jaak' on string millele on pandud väärtuseks Jaak")
print("c. pikkus = 16.5 on float see teisendab murdarvud ehk ujuvkomaarvud")
print("d. kas_käib_koolis = True on boolean millel saab olla ainult väärtuseks kas True või False")

vanus = 18
eesnimi = "Jaak"
pikkus = 16.5
kas_käib_koolis = True

print(isinstance(vanus, int))
print(isinstance(eesnimi, str))
print(isinstance(pikkus, float))
print(isinstance(kas_käib_koolis, bool))

input("Vajuta Enterit, et vaadata ülesannet 3.")

clear()

# Ülesanne 3
print("Ülesanne 3")

arv = random.randint(1,100)
print(f"Näed laual {arv} kommi.")
võtab = int(input("Mitu kommi soovid laualt ära võtta? "))
arv = arv - võtab
print(f"Laua peale on jäänud {arv} kommi.")

input("Vajuta Enterit, et vaadata ülesannet 4.")

clear()

# Ülesanne 4
print("Ülesanne 4")

ümbermõõt = float(input("Mis on puu ümbermõõt sentimeetrites? "))
läbimõõt = ümbermõõt / math.pi
print(f"Puu läbimõõt on {läbimõõt:.1f} cm.")

input("Vajuta Enterit, et vaadata ülesannet 5.")

clear()

# Ülesanne 5
print("Ülesanne 5")

N = float(input("Sisesta maatüki pikkus meetrites: "))
M = float(input("Sisesta maatüki laius meetrites: "))

diagonaal = math.sqrt(N**2 + M**2)
print(f"Maatüki diagonaal on {diagonaal:.1f} m.")

input("Vajuta Enterit, et vaadata ülesannet 6.")

clear()

# Ülesanne 6
print("Ülesanne 6")

print("Kiirust ei saa, kui aeg on jagatud teepikkusega vaid teepikkus on jagatud ajaga")

aeg = float(input("Mitu tundi kulus sõiduks? "))
teepikkus = float(input("Mitu kilomeetrit sõitsid? "))
kiirus = teepikkus / aeg

print(f"Sinu kiirus oli {kiirus:.0f} km/h")

input("Vajuta Enterit, et vaadata ülesannet 7.")

clear()

# Ülesanne 7
print("Ülesanne 7")

arv1 = int(input("Sisesta esimene täisarv: "))
arv2 = int(input("Sisesta teine täisarv: "))
arv3 = int(input("Sisesta kolmas täisarv: "))
arv4 = int(input("Sisesta neljas täisarv: "))
arv5 = int(input("Sisesta viies täisarv: "))

summa = arv1 + arv2 + arv3 + arv4 + arv5
keskmine = summa / 5

print("Arvude summa on", summa)
print("Arvude keskmine väärtus on", keskmine)

jagaja = int(input("Sisesta jagaja (täisarv peale nulli): "))

print("Täisarvuline osa:", summa // jagaja)
print("Jääk:", summa % jagaja)

input("Vajuta Enterit, et vaadata ülesannet 8.")

clear()

# Ülesanne 8
print("Ülesanne 8")

print("   @..@")
print("   (----)")
print("  (\\__//)")
print('^^ "" ^^')

input("Vajuta Enterit, et vaadata ülesannet 9.")

clear()

# Ülesanne 9
print("Ülesanne 9")

print("""Arvutame kolmnurga ümbermõõdu. 
Loo kolm täisarvulist muutujat a, b, c. Kasuta valem, mis arvutab kolmnurga ümbermõõdu (P=a+b+c)""")

a = 8
b = 12
c = 12

P = a + b + c
print(f"Kolmnurga ümbermõõt on, {P:.1f}")

input("Vajuta Enterit, et vaadata ülesannet 10.")

clear()

# Ülesanne 10
print("Ülesanne 10")

hind = 12.90
P = int(input("Mitu inimest jagab pitsat? "))

jootraha = hind * 0.10
kokku = hind + jootraha
igaühe_osa = kokku / P

print(f"Igaüks maksab {igaühe_osa:.2f} €.")

input("Vajuta Enterit, et vaadata ülesannet 10.")

clear()


# Ülesanne 11
print("Ülesanne 11: Ülesande 3 näidis try-except koodiga") # Ülesanne 3 näidis try-except

arv = random.randint(2,100)
print(f"Näed laual {arv} kommi.")

while True:
    try:
        võtab = int(input("Mitu kommi soovid laualt ära võtta? "))
        if (võtab < 0):
            print("Sisesta positiivne täisarv!")
        elif (võtab > arv):
            print("Laual pole nii palju komme, kui sa võtta tahad!")
        else:
            arv = arv - võtab 
            tekst = "kommi"
            if (arv == 1):
                tekst = "komm"
            print(f"Laua peale on jäänud {arv} {tekst}.")
            break
    except BaseException:
        print("Sisesta positiivne arv!")
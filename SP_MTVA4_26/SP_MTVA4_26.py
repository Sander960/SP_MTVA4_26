import os
import random
import math

# leidsin lahenduse, et peale igat harjutust tuleb puhas leht https://stackoverflow.com/a/684344
def clear():
    os.system('cls')

# Ülesanne 1
print("Tere maailm!") 
nimi = input("Mis on sinu nimi? ")
print(f"Tere maailm! Tervitan sind, {nimi}!")
vanus = input("Mis on sinu vanus? ")
print(f"Tere maailm! Tervitan sind, {nimi}! Sa oled {vanus} aastat vana.")

input("Vajuta Enterit, et vaadata ülesannet 2.")

clear()

# Ülesanne 2
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

arv = random.randint(1,100)
print(f"Näed laual {arv} kommi.")
võtab = int(input("Mitu kommi soovid laualt ära võtta? "))
arv = arv - võtab
print(f"Laua peale on jäänud {arv} kommi.")

input("Vajuta Enterit, et vaadata ülesannet 4.")

clear()

# Ülesanne 4

ümbermõõt = float(input("Mis on puu ümbermõõt sentimeetrites? "))
läbimõõt = ümbermõõt / math.pi
print(f"Puu läbimõõt on {läbimõõt:.1f} cm.")

input("Vajuta Enterit, et vaadata ülesannet 5.")

clear()

# Ülesanne 5

N = float(input("Sisesta maatüki pikkus meetrites: "))
M = float(input("Sisesta maatüki laius meetrites: "))

diagonaal = math.sqrt(N**2 + M**2)
print(f"Maatüki diagonaal on {diagonaal:.1f} m.")

input("Vajuta Enterit, et vaadata ülesannet 6.")

clear()

# Ülesanne 6

print("Kiirust ei saa, kui aeg on jagatud teepikkusega vaid teepikkus on jagatud ajaga")

aeg = float(input("Mitu tundi kulus sõiduks? "))
teepikkus = float(input("Mitu kilomeetrit sõitsid? "))
kiirus = teepikkus / aeg

print(f"Sinu kiirus oli {kiirus:.0f} km/h")

input("Vajuta Enterit, et vaadata ülesannet 7.")

clear()


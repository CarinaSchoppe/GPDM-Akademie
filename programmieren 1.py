# PASSWORT: Marbach23#



"""

+,-,*,/ -> Mathe
wir kennen: und, oder, nicht, ()
blöcke, bereiche: und leerzeichen
if, else,
print(irgendwas reinschreiben)

variable = inhalt

strings, integer, char, boolean, ....



"""

# wort = input() # -> Egal was ich hier eintippe: Da kommt immer erst nen string raus

import random

stats = {"Leben": 10, "Damage": 5, "Ausdauer": 20, "Geld": 0}
print("Wie ist dein Name?")
name = input()

print("Du", name, "bist nun ein Abenteurer. Du ziehst los. Wo geht deine Reise denn hin? (riskant 2, gut 1)")

guter_weg = 1
riskanter_weg = 2

antwort_weg = int(input())  # "das kann 1 oder 2 sein / theoretisch"

if antwort_weg == 1:
    print("Du gehst den guten Weg, Lusche")
elif antwort_weg == 2:
    print("Nur die Sparten kommen in den Garten, und du wohl auch. Viel Glück...")
else:
    print("Du kannst wohl auch nicht lesen... gehst jetzt wohl direkt in die Hölle, also Weg 2")
    antwort_weg = 2

print("Du hast dich also für den Weg entschieden, interessante Wahl....")
print("Auf deinem Weg kann es sein, dass du vielen Feinden begegnest... Oh nein... ein Feind... Lul")
print("Ein wildes Pikachu ist aufgetaucht...")
print("Wie entscheidest du dich: (Kampf, Flucht)")


def kampf(stats):

    begegnungs_entscheidung = input()

    if begegnungs_entscheidung == "Kampf":
        print("Du kannst nun ATK einsetzen... ")
        pikachu_hp = random.randint(5, 10)
        while pikachu_hp > 0:
            print("Du hast zur Auswahl: (Mampf (1), Schlag (2), Verführung (3), Multi-Schlag (4)")
            kampf_entscheidung = int(input())
            if kampf_entscheidung == 1:
                print("Wir werden fetter")
                if stats["Leben"] < 10:
                    stats["Leben"] = stats["Leben"] + 1
                    print("Du hast nun:", stats["Leben"])
                else:
                    print("Leben ist bereits voll du honk")
            elif kampf_entscheidung == 4:
                print("wie oft haust du zu?")
                zuhauen_anzahl = int(input())
                if zuhauen_anzahl > stats["Ausdauer"]:
                    print("geht nicht")
                else:
                    for wiederholung in range(zuhauen_anzahl):
                        schaden = stats["Damage"] * (random.randint(1, 8)/10)
                        print("ich schlage pikachu")
                        pikachu_hp -= schaden  # spart mir das pikachu_hp = pikachu_hp
                        print("Du hast dem Pikachu", schaden, " an schaden gemacht")
                        print("Das Pikachu hat noch", pikachu_hp, " an leben")
                        if pikachu_hp <= 0:
                            break
            elif kampf_entscheidung == 2:
                schaden = stats["Damage"] * 0.5  # schaden den schlag machen kann ist 0.5
                pikachu_hp = pikachu_hp - schaden
                print("Du hast dem Pikachu", schaden, " an schaden gemacht")
                print("Das Pikachu hat noch", pikachu_hp, " an leben")
            else:
                print("Junge / Mädel, du willst was mit Pichachu, das Ding ist ne Maus...")
            if pikachu_hp > 0:
                print("Pikachu setzt Hinternbombe ein")
                stats["Leben"] = stats["Leben"] - 4
                print("Du hast 4 schaden gekriegt", stats["Leben"], "hast du noch übrig")
                if stats["Leben"] < 1:
                    print("kampf beendet, du hast verkackt")
                    break  # zwanghaftes beenden der while schleife

        if stats["Leben"] > 1:
            print("Du hast Pikachu besiegt")
            print("du Bekommst 5 Geld und +1 Stärke")
            stats["Damage"] = stats["Damage"] + 1
            stats["Geld"] += 5



    elif begegnungs_entscheidung == "Flucht":
        print("Du hast Glück gehabt und konntest NOCH fliehen")
    else:
        print("Wer sich nicht entscheiden kann der flüchtet...")

    return stats




### for scheife, while schleife


#leben, damage, geld, ausdauer = kampf(stats["Leben"], stats["Damage"], stats["Geld"], stats["Ausdauer"])  # (leben, damage, geld, ausdauer)
stats = kampf(stats)
print("Leben:", stats["Leben"])
print("Damage:", stats["Damage"])
print("Geld:", stats["Geld"])
print("Ausdauer:", stats["Ausdauer"])
# Marbach23#
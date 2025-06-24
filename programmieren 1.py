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

leben = 10
essen = 100
damage = 5
ausdauer = 20
geld = 0
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





begegnungs_entscheidung = input()

if begegnungs_entscheidung == "Kampf":
    print("Du kannst nun ATK einsetzen... ")
    pikachu_hp = 4
    while pikachu_hp > 0:
        print("Du hast zur Auswahl: (Mampf (1), Schlag (2), Verführung (3), Multi-Schlag (4)")
        kampf_entscheidung = int(input())
        if kampf_entscheidung == 1:
            print("Wir werden fetter")
            if leben < 10:
                leben = leben + 1
                print("Du hast nun:", leben)
            else:
                print("Leben ist bereits voll du honk")
        elif kampf_entscheidung == 4:
            schaden = 0.1 * damage
            print("wie oft haust du zu?")
            zuhauen_anzahl = int(input())
            if zuhauen_anzahl > ausdauer:
                print("geht nicht")
            else:
                for wiederholung in range(zuhauen_anzahl):
                    print("ich schlage pikachu")
                    pikachu_hp -= schaden # spart mir das pikachu_hp = pikachu_hp
                    print("Du hast dem Pikachu", schaden, " an schaden gemacht")
                    print("Das Pikachu hat noch", pikachu_hp, " an leben")
                    if pikachu_hp <= 0:
                        break
        elif kampf_entscheidung == 2:
            schaden = damage * 0.5  # schaden den schlag machen kann ist 0.5
            pikachu_hp = pikachu_hp - schaden
            print("Du hast dem Pikachu", schaden, " an schaden gemacht")
            print("Das Pikachu hat noch", pikachu_hp, " an leben")
        else:
            print("Junge / Mädel, du willst was mit Pichachu, das Ding ist ne Maus...")

        print("Pikachu setzt Hinternbombe ein")
        leben = leben - 4
        print("Du hast 4 schaden gekriegt", leben, "hast du noch übrig")
        if leben < 1:
            print("kampf beendet, du hast verkackt")
            break  # zwanghaftes beenden der while schleife

    if leben > 1:
        print("Du hast Pikachu besiegt")
        print("du Bekommst 5 Geld und +1 Stärke")
        damage = damage + 1
        geld += 5



elif begegnungs_entscheidung == "Flucht":
    print("Du hast Glück gehabt und konntest NOCH fliehen")
else:
    print("Wer sich nicht entscheiden kann der flüchtet...")

# Marbach23#


### for scheife, while schleife








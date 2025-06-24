class Kunde:
    def __init__(self, name, geld, kontonummer):
        self.name = name
        self.geld = geld
        self.kontonummer = kontonummer
        self.transaktionen = []

    def kontoauszug_einfordern(self):
        for transaktion in self.transaktionen:
            print(transaktion)

    def geld_verdienen(self, betrag):
        pass


class Bank:
    def __init__(self, name):
        self.name = name
        self.kunden = []
        self.transaktionen = {}
        self.ids = 0

    def add_kunde(self, kunde):
        self.kunden.append(kunde)

    def remove_kunde(self, kunde):
        self.kunden.remove(kunde)

    def geld_auszahlen(self, kunde, betrag):
        if kunde.geld < betrag:
            print("Du hast nicht genug Geld")
            return
        kunde.geld -= betrag
        print("Du hast", betrag, "euro ausgezahlt!")

    def geld_einzahlen(self, kunde, betrag):
        kunde.geld += betrag
        print("Du", kunde.name," hast", betrag, "euro eingezahlt!")
        print("Du hast nun", kunde.geld, "euro")

    def geld_überweisen(self, sender, empfänger, betrag):
        #kennen wir den empfänger
        if empfänger not in self.kunden:
            print("Der Empfänger ist nicht in unserer Bank")
            return
        if sender.geld >= betrag:
            sender.geld -= betrag
            print("Du", sender.name, " hast", betrag, "euro an", empfänger.name, "gegeben")
            print("Du hast jetzt", sender.geld, "euro")
            empfänger.geld += betrag
            print("Du", empfänger.name, " hast", betrag, "euro von", sender.name, "empfangen")
            print("Du hast jetzt", empfänger.geld, "euro")
            self.transaktionen_ausgeben(sender, betrag, empfänger)

        else:
            print("Du hast nicht genug Geld")




    def transaktion_zwischen_kunden_hinzufügen(self, sender, empfänger, betrag):
        transaktion = "Sender: " + sender.name, "Empfänger: " + empfänger.name, "Betrag: " + str(betrag)
        self.transaktionen[self.ids] = transaktion
        empfänger.transaktionen.append(self.ids)
        sender.transaktionen.append(self.ids)
        self.ids += 1

    def transaktion_einzelperson_hinzufügen(self, kunde, betrag):

        if betrag > 0:
            methode = "einzahlen"
        else:
            methode = "auszahlen"
        transaktion = "Kunde: " + kunde.name, "Betrag: " + str(betrag) + "euro" + methode
        self.transaktionen[self.ids] = transaktion
        kunde.transaktionen.append(self.ids)
        self.ids += 1

    def transaktionen_ausgeben(self, kunde, betrag, Kunde2=None):
        if Kunde2 is None:
            self.transaktion_einzelperson_hinzufügen(kunde, betrag)
        else:
            self.transaktion_zwischen_kunden_hinzufügen(kunde, Kunde2, betrag)


Menschen = [Kunde("Steve", 1000, "1234"), Kunde("Max", 2000, "1235"), Kunde("Anna", 3000, "1236")]


bank = Bank("Bank")

bank.add_kunde(Menschen[0])
bank.add_kunde(Menschen[1])
bank.add_kunde(Menschen[2])

bank.geld_einzahlen(Menschen[0], 100)
bank.geld_einzahlen(Menschen[1], 200)
bank.geld_einzahlen(Menschen[2], 300)

bank.geld_überweisen(Menschen[0], Menschen[1], 100)
bank.geld_überweisen(Menschen[1], Menschen[2], 100)

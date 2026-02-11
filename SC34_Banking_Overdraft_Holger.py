# DIFFICULTY: 4
# Für die Verwaltung eines simplen Kontos nutzen wir eine Variable, welche den vorhandenen
# Betrag auf dem Konto speichert.

# TASK: Implementiere zwei Funktionen, jeweils eine zum ein- und auszahlen von
#       beliebigen Summen anhand eines Inputs. Stelle dabei sicher, dass unzulässige
#       Eingaben, zu große/kleine Summen und mögliche weitere Errors abgefangen werden.
#       Achte auch auf präzise und verständliche Ausgaben bzw. Fehlermeldungen für Nutzer*innen.
#
# CHALLENGE: Implementiere zusätzlich eine Funktion, die einen flexiblen Überzug erlaubt
#            und für diesen entsprechend Zinsen berechnet.

my_bank_account = 1000.00
'''
def withdraw(amount: float, bank_account: float) -> float:
    pass

def deposit(amount: float) -> None:
    pass

def set_overdraft(overdraft: float) -> float:
    pass
'''
my_bank_account = 1000.00
your_bank_account = 1500.00
his_bank_account = 900.00
her_bank_account = 100_000.00

bank_accounts = ["my_bank_account", "your_bank_account", "his_bank_account", "her_bank_account"]
bank_ammounts = [1_000.0, 1_500.0, 900.0, 100_000.0]
bank_overdraft = [0.0, 0.0, 0.0, 50_000.0]


def log_in_bank_account():
    print("Bitte geben Sie Ihren Bankaccount ein, um sich einzuloggen.")
    bank_account = input("Bankaccount: ")
    if bank_account == "q":
        tekniker_c0de = input("Tekniker C0de: ")
        if tekniker_c0de == "gfn" :
            exit("################################\n##Bankautomat heruntergefahren##\n################################")
        else:
            log_in_bank_account()
            exit()
    print("-----------------------------------")
    acc = False
    # Überprüfe den Account
    acc = False
    while acc is False:
        if bank_account not in bank_accounts:
            print("Bitte geben Sie einen gültigen Bankaccount an.\nBeispiel:\nits_bank_account\ntheir_bank_account")
            bank_account = input("Bankaccount: ")
            if bank_account == "q":
                tekniker_c0de = input("Tekniker C0de: ")
                if tekniker_c0de == "gfn" :
                    exit("################################\n##Bankautomat heruntergefahren##\n################################")
                else:
                    log_in_bank_account()
                    exit()
            print("-----------------------------------")
        else:
            for x in range(len(bank_accounts)):
                if bank_accounts[x] == bank_account:
                    acc_nr = x
                    acc = True
                    direct_banking(acc_nr, acc)
                    break


def direct_banking(acc_nr, acc):
    # Ist richtig eingeloggt?
    if acc is not True:
        log_in_bank_account()
        exit()
    while acc is True:
        # Menüauswahl
        print("Menü\n1 Kontostand\n2 Abheben\n3 Einzahlen\n4 Dispositionskredit\n5 Ausloggen\n-----------------------------------")
        eingabe = input("Auswahl: ")
        print("-----------------------------------")
        # Weiterleitungen
        if eingabe == "1":
            print(f"Guthaben: {bank_ammounts[acc_nr]:.2f} €")
            print("-----------------------------------")
        elif eingabe == "2":
            print("Bitte geben Sie den Abbuchungsbetrag ein.")
            amount = input("Betrag: ")
            print("-----------------------------------")
            withdraw(amount, bank_overdraft[acc_nr], acc_nr, acc)
        elif eingabe == "3":
            print("Bitte geben Sie den Einzahlungsbetrag ein.")
            amount = input("Betrag: ")
            print("-----------------------------------")
            deposit(amount, acc_nr, acc)
        elif eingabe == "4":
            pass
            print("Bitte geben Sie den gewünschten Dispositionskredit ein.")
            amount = input("Betrag: ")
            print("-----------------------------------")
            set_overdraft(amount, acc_nr, acc)
        elif eingabe == "5":
            acc = False
            print("Sie wurden erfolgreich ausgeloggt!\n-----------------------------------")
            log_in_bank_account()
        else:
            print("Fehleingabe!\nBitte wählen Sie eine Auswahl, indem Sie die entsprechende Zahl eingeben.\nBeispiel:\n1\n4")


def set_overdraft(overdraft, bank_account, acc):
    # Ist richtig eingeloggt?
    if acc is not True:
        log_in_bank_account()
        exit()
    # Überprüfe den Betrag
    od = False
    while od is False:
        try:
            overdraft = float(overdraft)
        except Exception:
            pass
        if type(overdraft) is not float and type(overdraft) is not int:
            print("Bitte gib die gewünschte Höhe des Dispositionskredits als Zahl ein.\nBeispiel:\n100\n10.2")
            overdraft = input("Betrag: ")
            print("-----------------------------------")
        elif overdraft < 0:
            print("Bitte gib die gewünschte Höhe des Dispositionskredits größer als 0 ein.\nBeispiel:\n100\n10.2")
            overdraft = input("Betrag: ")
            print("-----------------------------------")
        elif overdraft > (bank_ammounts[bank_account] * 0.5):
            print("Bitte gib eine gewünschte Höhe des Dispositionskredits ein, welche maximal deinem halben Guthaben entspricht.")
            overdraft = input("Betrag: ")
            print("-----------------------------------")
        elif type(overdraft) is float or type(overdraft) is not float:
            overdraft = float(overdraft)
            od = True
            # Passe den Dispo an
            temp = overdraft
            str1 = f"Dispositionskredit davor: {bank_overdraft[bank_account]:.2f} €"
            str2 = f"Dispositionskredit neu: {temp:.2f} €"
            str3 = f"Zinssatz: 19.99 % p.A."
            # Formatierung
            if len(str1) >= len(str2) and len(str1) >= len(str3):
                laenge = len(str1)
                diff1 = laenge - len(str1)
                diff2 = laenge - len(str2)
                diff3 = laenge - len(str3)
            elif len(str2) >= len(str1) and len(str2) >= len(str3):
                laenge = len(str2)
                diff1 = laenge - len(str1)
                diff2 = laenge - len(str2)
                diff3 = laenge - len(str3)
            else:
                laenge = len(str3)
                diff1 = laenge - len(str1)
                diff2 = laenge - len(str2)
                diff3 = laenge - len(str3)
            # Ausgabe
            print(f"Dispositionskredit davor:{" " * diff1} {bank_overdraft[bank_account]:.2f} €")
            bank_overdraft[bank_account] = temp
            print(f"Dispositionskredit neu:{" " * diff2} {temp:.2f} €\nZinssatz:{" " * diff3} 19.99 % p.A.\n-----------------------------------")
        else:
            exit("###################################\nUnbekannter Fehler!\nBitte wenden Sie sich an einen Sachbearbeiter!\nEs wurde KEIN Geld übertrage!\n###################################")


def deposit(amount, bank_account, acc):
    # Ist richtig eingeloggt?
    if acc is not True:
        log_in_bank_account()
        exit()
    # Überprüfe den Betrag
    amo = False
    while amo is False:
        try:
            amount = float(amount)
            if amount > 0:
                amo = True
                # Buche den Betrag ab
                temp = bank_ammounts[bank_account] + amount
                str1 = f"Guthaben vorher: {bank_ammounts[bank_account]:.2f} €"
                str2 = f"Einzahlung: {amount:.2f} €"
                str3 = f"Guthaben neu: {temp:.2f} €"
                # Formatierung
                if len(str1) >= len(str2) and len(str1) >= len(str3):
                    laenge = len(str1)
                    diff1 = laenge - len(str1)
                    diff2 = laenge - len(str2)
                    diff3 = laenge - len(str3)
                elif len(str2) >= len(str1) and len(str2) >= len(str3):
                    laenge = len(str2)
                    diff1 = laenge - len(str1)
                    diff2 = laenge - len(str2)
                    diff3 = laenge - len(str3)
                else:
                    laenge = len(str3)
                    diff1 = laenge - len(str1)
                    diff2 = laenge - len(str2)
                    diff3 = laenge - len(str3)
                # Ausgabe
                print(f"Guthaben vorher:{" " * diff1} {bank_ammounts[bank_account]:.2f} €\nEinzahlung:{" " * diff2} {amount:.2f} €")
                # Realisierung der Abbuchung
                bank_ammounts[bank_account] = temp
                print(f"Guthaben neu:{" " * diff3} {temp:.2f} €\n-----------------------------------")
            elif amount < 0:
                print("Bitte gib einen Einzahlungsbetrag größer als 0 ein.\nBeispiel:\n100\n10.2")
                amount = input("Betrag: ")
                print("-----------------------------------")
        except Exception:
            if type(amount) is not float and type(amount) is not int:
                print("Bitte gib den Einzahlungsbetrag als Zahl ein.\nBeispiel:\n100\n10.2")
                amount = input("Betrag: ")
                print("-----------------------------------")
            else:
                exit("###################################\nUnbekannter Fehler!\nBitte wenden Sie sich an einen Sachbearbeiter!\nEs wurde KEIN Geld übertrage!\n###################################")


def withdraw(amount, overdraft, bank_account, acc):
    # Ist richtig eingeloggt?
    if acc is not True:
        log_in_bank_account()
        exit()
    # Überprüfe den Betrag
    amo = False
    while amo is False:
        try:
            amount = float(amount)
            if amount >= 0 and amount <= (overdraft + bank_ammounts[bank_account]):
                amo = True
                # Zinsen pro Abbuchung
                interest = 0
                if amount > bank_ammounts[bank_account]:
                    overflow = amount - bank_ammounts[bank_account]
                    interest = overflow * 0.1999
                # Buche den Betrag ab
                temp = bank_ammounts[bank_account] - (amount + interest)
                str1 = f"Guthaben vorher: {bank_ammounts[bank_account]:.2f} €"
                str2 = f"Abbuchung: {amount:.2f} €"
                str3 = f"Guthaben neu: {temp:.2f} €"
                # Formatierung
                if len(str1) >= len(str2) and len(str1) >= len(str3):
                    laenge = len(str1)
                    diff1 = laenge - len(str1)
                    diff2 = laenge - len(str2)
                    diff3 = laenge - len(str3)
                elif len(str2) >= len(str1) and len(str2) >= len(str3):
                    laenge = len(str2)
                    diff1 = laenge - len(str1)
                    diff2 = laenge - len(str2)
                    diff3 = laenge - len(str3)
                else:
                    laenge = len(str3)
                    diff1 = laenge - len(str1)
                    diff2 = laenge - len(str2)
                    diff3 = laenge - len(str3)
                # Ausgabe
                print(f"Guthaben vorher:{" " * diff1} {bank_ammounts[bank_account]:.2f} €\nAbbuchung:{" " * diff2} {amount:.2f} €")
                # Realisierung der Abbuchung
                bank_ammounts[bank_account] = temp
                print(f"Guthaben neu:{" " * diff3} {temp:.2f} €\n-----------------------------------")
            elif amount == 0:
                amo = True
                # Buche den Betrag ab
                str1 = f"Guthaben vorher: {bank_ammounts[bank_account]:.2f} €"
                str2 = f"Abbuchung: {amount:.2f} €"
                str3 = f"Guthaben neu: {bank_ammounts[bank_account]:.2f} €"
                # Formatierung
                if len(str1) >= len(str2) and len(str1) >= len(str3):
                    laenge = len(str1)
                    diff1 = laenge - len(str1)
                    diff2 = laenge - len(str2)
                    diff3 = laenge - len(str3)
                elif len(str2) >= len(str1) and len(str2) >= len(str3):
                    laenge = len(str2)
                    diff1 = laenge - len(str1)
                    diff2 = laenge - len(str2)
                    diff3 = laenge - len(str3)
                else:
                    laenge = len(str3)
                    diff1 = laenge - len(str1)
                    diff2 = laenge - len(str2)
                    diff3 = laenge - len(str3)
                # Ausgabe
                print(f"Guthaben vorher:{" " * diff1} {bank_ammounts[bank_account]:.2f} €\nAbbuchung:{" " * diff2} {amount:.2f} €")
                print(f"Guthaben neu:{" " * diff3} {bank_ammounts[bank_account]:.2f} €\n-----------------------------------")
            elif amount < 0:
                print("Bitte gib einen Abbuchungsbetrag größer als 0 ein.\nBeispiel:\n100\n10.2")
                amount = input("Betrag: ")
                print("-----------------------------------")
            elif amount > (overdraft + bank_ammounts[bank_account]):
                print("Bitte gib einen Abbuchungsbetrag ein, welcher maximal deinem Guthaben und Dispositionskredits entspricht.")
                amount = input("Betrag: ")
                print("-----------------------------------")
        except Exception:
            if type(amount) is not float and type(amount) is not int:
                print("Bitte gib den Abbuchungsbetrag als Zahl ein.\nBeispiel:\n100\n10.2")
                amount = input("Betrag: ")
                print("-----------------------------------")
            else:
                exit("###################################\nUnbekannter Fehler!\nBitte wenden Sie sich an einen Sachbearbeiter!\nEs wurde KEIN Geld übertrage!\n###################################")


log_in_bank_account()
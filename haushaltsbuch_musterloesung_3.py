''''Haushaltsbuch'''
print('*************************************')
print('                                     ')
print('           Haushaltsbuch             ')
print('                                     ')
print('*************************************')
print()
print('Menü')
print('1 - Einen Eintrag machen?')
print('2 - Keinen Eintrag machen?')
eingabe = input('Treffe deine Auswahl: ')
while True:
    if eingabe == '2':
        break
    elif eingabe == '1':
    
        '''Variable für das Wocheneinkaufsbudget erstellen: budget'''
        budget = 30.0
        print('Dir stehen wöchentlich %.2f' % budget, 'Euro für Obst zu Verfügung.')
        antwort = None
        antwort = input('Willst du das Budget anpassen? (Ja/ Nein) ')
        if antwort == "Ja":
            budget= float(input('Bitte gebe den neuen Betrag ein: '))
            print('Dein neues Budget beträgt %.2f' % budget, 'Euro')
        if antwort == "ja":
            budget= float(input('Bitte gebe den neuen Betrag ein: '))
            print('Dein neues Budget beträgt %.2f' % budget, 'Euro')
        if antwort == "JA":
            budget= float(input('Bitte gebe den neuen Betrag ein: '))
            print('Dein neues Budget beträgt %.2f' % budget, 'Euro')
        else:
            print()
            
        '''Es soll der Wochendurchschnitt für den Einkauf von Obst berechnet werden'''
        '''Liste mit dem Namen obst erstellen'''
        obst = []

        '''Eingabe für Woche 1, Woche 2, Woche 3 und Woche 4 ermöglichen'''
        wo1 = float(input('Ausgabe für Obst in Woche 1: '))
        obst.append(wo1)
        wo2 = float(input('Ausgabe für Obst in Woche 2: '))
        obst.append(wo2)
        wo3 = float(input('Ausgabe für Obst in Woche 3: '))
        obst.append(wo3)
        wo4 = float(input('Ausgabe für Obst in Woche 4: '))
        obst.append(wo4)

        '''Variable für den Durchschnitt erstellen: durchschnitt'''
        durchschnitt = None

        '''Den Wochendurchschnitt berechnen und ausdrucken'''
        durchschnitt = sum(obst) / len(obst)
        print('Der Wochendurchschnitt für den Einkauf von Obst beträgt %.2f' % durchschnitt, 'Euro.')

        '''Berechnen ob das Budget überschritten wurde und eine sinnvolle Nachricht ausgeben'''
        if durchschnitt < budget:
            print('Das Budget wurde nicht ausgeschöpft, gönn dir eine Belohnung.')
            
        print()
        abbruch = input('noch eine Berechnung durchführen? (J/N)')
        if abbruch == 'J':
            print()
        if abbruch == 'N':
            break

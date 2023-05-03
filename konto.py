import time
konto = [0]

def kontostand():
    print('\nDein aktueller Kontostand beträgt', sum(konto))
    print()
    
def ueberweisung():
    print('Kontonummer eingeben: ')
    kto_nummer = int(input('>'))
    print('Betrag eingeben: ')
    ue_betrag = int(input('>'))
    while True:
        if ue_betrag > sum(konto):
            print('Betrag ist zu hoch')
            break
            
        else:
            konto.append(-ue_betrag)
          
    
while True:
    print(' *** Deine Zukunftsbank ***')
    print('Bitte zur Face ID vor die Kamera stellen\n')
    time.sleep(0.5)
    print('.')
    time.sleep(0.5)   
    print('')
    print('*************************************')
    print('           Kontomenü                 ')
    print('*************************************')
    print()
    print('Menü')
    print('1 - Einen Einzahlung machen?')
    print('2 - Geld abheben?')
    print('3 - Kontostand anzeigen')
    print('4 - Überweisung durchführen')
    print('5 - Abbrechen')
    eingabe = input('> ')
    
    if eingabe == '1':
        plus = int(input('> '))
        konto.append(plus)
        kontostand()
    elif eingabe == '2':
        minus = int(input('> '))
        konto.append(-minus)
        kontostand()
    elif eingabe == '3':
        kontostand()
    elif eingabe == '4':
        ueberweisung()
    elif eingabe == '5':
        break
        
                
                
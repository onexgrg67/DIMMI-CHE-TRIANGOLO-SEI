def init():
    print("DIMMI CHE TRIANGOLO SEI")
    l1 = input("Inserisci il lato minore: ")
    l2 = input("Inserisci il lato medio: ")
    l3 = input("Inserisci il lato maggiore: ")

    if(str(l1)=="" or str(l2)=="" or str(l3)==""):
        print("Completa l'inserimento dei dati")
        init()
    elif(int(l1)>0 and int(l2)>=int(l1) and int(l3)>=int(l2)):
        print("I dati sono inseriti correttamente")
        if (l1+l2>l3):
            print("I dati inseriti individuano un triangolo")
            if (l1 == l3):
                print("IL triangolo è equilatero")
            elif (l1 == l2 or l2 == l3):
                print("Il triangolo è scaleno")
            else:
                print("Il triangolo è isoscele")
        else:
            print("I dati inseriti non individuano un triangolo")
    else:
        print("I dati non sono inseriti correttamente")
        init()
init()
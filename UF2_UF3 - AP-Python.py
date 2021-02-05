import csv
import pandas
import function as fc

def main():
    print("*****************************************")
    print("********* Gestió d'alumnes **************")
    print("*****************************************")

    print("----Menu inicial----")
    print("1. Introdueir alumnes")
    print("2. Mostrar alumnes")
    print("3. Analitzar registres")
    menu = int(input("Introdueix l'opcio: ")) #selecció de les opcions del menu
    while (menu<1 or menu>3):
        menu = int(input("Introdueix l'opcio correctament: "))
    print("")
    if (menu==1):
        fc.add_menu()
    elif (menu==2):
        fc.show_menu()
    elif (menu==3):
        fc.analyze_menu()


if __name__ == '__main__':
    main()
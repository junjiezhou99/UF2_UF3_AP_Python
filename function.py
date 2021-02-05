import csv
import pandas

def add_menu(): #Introduir alumnes
    number = int(input("Indica el nombre d'alumnes que vols introduir: "))
    while (number<0):
        number = int(input("Indica el nombre correctament: "))
    err=0
    test_header=0

    for i in range(number):
        #introduccion y validacion de los datos
        while (err==0):
            try:
                student_ID = int(input("Introdueix l'identificador: "))
                err=1
            except:
                print("Introdueix l'identificador correctament")
        first_name = input("Introdueix el nom de l'estudiant: ")
        last_name = input("Introdueix el cognom de l'estudiant: ")
        subject = input("Introdueix l'assignatura: ")
        while (err==1):
            try:
                grade = int(input("Introdueix la nota: "))
                err=0
            except:
                print("Introdueix la nota correctament")

        #introduccion al csv
        with open('algo.csv', 'a', newline="") as csvfile:
            head = ['student_ID', 'first_name', 'last_name', 'subject', 'grade']
            writeCSV = csv.DictWriter(csvfile, fieldnames=head)
            #Si el header esta puesto no repetira
            if (test_header==0):
                writeCSV.writeheader()
                test_header=1
            writeCSV.writerow({'student_ID': student_ID, 'first_name': first_name, 'last_name': last_name, 'subject': subject, 'grade': grade})

def show_menu(): #Mostrar alumnes
    with open('algo.csv') as csvfile:
        readCSV = csv.reader(csvfile)
        for row in readCSV:
            try:
                print(f'\t {row[0]}, {row[1]}, {row[2]}, {row[3]}, {row[4]}.')
            except:
                print("error")

def analyze_menu(): #Analitzar registres
    print("----Menu registres----")
    print("1. Mostrar el total de registres")
    print("2. Els 2 primers registres")
    print("3. Els 2 ultims registres")
    register=int(input("Quants registres vol consultar: "))
    while (register<1 or register>3):
        register = int(input("Introdueix els registres correctament: "))
    print("")
    df = pandas.read_csv('algo.csv')
    if (register==1):
        print(df)
    elif (register==2):
        print(df.head(2))
    elif (register==3):
        print(df.tail(2))

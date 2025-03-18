import csv
import re


def main():
    telefono = re.compile(r"^\+\d{2}[ -]*\d{3}[ -]*\d{3}[ -]*\d{4}$")
    #https://www.regextester.com/
    try:
        with open("contatti.csv") as f:
            csv_rdr = csv.reader(f, delimiter=',', quotechar='"',
                                 dialect="excel")
            for riga in csv_rdr:
                print(riga)
                if telefono.match(riga[2]):
                    print("Telefono valido")
                    t1= re.sub(r"^\+39[ -].+","",riga[2])
                    t2= re.sub(r"(\+39)[ -](\d{3})[ -](\d+)",r"(\1) \2/\3",riga[2])
                    # tmp=r"[a-z]{1,5}"
                    print(t2)
                else:
                    print("Telefono non valido")

    except FileNotFoundError:
        print("File non trovato")
    


if __name__ == '__main__':
    main()
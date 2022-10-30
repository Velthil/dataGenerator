import random
import oracleDBconn

class generator:

    def __init__(self):
        print('Generator')

    def get(self, set, num):
        if set == 0:
            return self.gen0(num)
        elif set == 1:
            return self.gen1(num)
        elif set == 2:
            return self.gen2(num)
        elif set == 3:
            return self.gen3(num)
        elif set == 4:
            return self.gen4(num)
        elif set == 5:
            return self.gen5(num)
        elif set == 6:
            return self.gen6(num)
        elif set == 7:
            return self.gen7(num)
        elif set == 8:
            return self.gen8(num)
        elif set == 9:
            return self.gen9(num)

    # Krwiodawcy
    def gen0(self, num):
        conn = oracleDBconn.DbConnection()
        conn.execute('SELECT kod_pocztowy FROM miasta')
        isInDB = conn.getData()
        del conn



        return 0

    # Dyskwalifikacje
    def gen1(self, num):
        print('Dyskwalifikacje')
        return 0

    # Miasta
    def gen2(self, num):
        conn = oracleDBconn.DbConnection()
        conn.execute('SELECT kod_pocztowy FROM miasta')
        isInDB = conn.getData()
        del conn

        with open(r'data/kodyMiasta.txt', 'r', encoding='utf-8') as fp:
            rawData = fp.readlines()

        data = []
        for row in rawData:
            if str(row).split()[0] not in isInDB:
                data.append(row)

        x = len(data)
        print('Dostępne miasta:', x)
        if x == 0:
            return 0
        elif x < num:
            num = x;

        result = self.toList(random.choices(data, k=num))
        return result

    # Oddzial_RCKiK
    def gen3(self, num):
        print('Oddzial_RCKiK')
        return 0


    # Pracownicy
    def gen4(self, num):
        print('Pracownicy')
        return 0


    # Oddzial_terenowy
    def gen5(self, num):
        print('Oddzial_terenowy')
        return 0


    # Pobrania + Krew
    def gen6(self, num):
        print('Pobrania + Krew')
        return 0


    # Wyniki_badan
    def gen7(self, num):
        print('Wyniki_badan')
        return 0


    # Wydania_krwi
    def gen8(self, num):
        print('Wydania_krwi')
        return 0


    # Jednostki_docelowe
    def gen9(self, num):
        print('Jednostki_docelowe')
        return 0

    def toList(self, data):
        result = []
        for i in range(len(data)):
            result.append(str(data[i]).split())
        return result


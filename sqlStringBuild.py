import oracleDBconn

def genSQl(set, data):
    ins = 'INSERT INTO '
    val = 'VALUES '
    tables = ['Krwiodawcy', 'Dyskwalifikacje', 'Miasta', 'Oddzial_RCKiK', 'Pracownicy', 'Oddzial_terenowy',
              'Pobrania', 'Wyniki_badan', 'Wydania_krwi', 'Jednostki_docelowe']
    table = tables[set]

    if set == 0:
        return 0

    elif set == 1:
        return 0

    elif set == 2:
        fields = '(miasto, kod_pocztowy) '
        sqlSet = []
        for i in range(len(data)):
            sqlCommand = ins + tables[set] + " " + fields + val + "('" + data[i][1] + "', '" + data[i][0] + "')"
            sqlSet.append(sqlCommand)
        return sqlSet

    elif set == 3:
        return 0

    elif set == 4:
        return 0

    elif set == 5:
        return 0

    elif set == 6:
        return 0

    elif set == 7:
        table2 = ['Krew']
        return 0

    elif set == 8:
        return 0

    elif set == 9:
        return 0







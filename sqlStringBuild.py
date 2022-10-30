import oracleDBconn

def genSQl(set, data):
    ins = 'INSERT INTO '
    val = 'VALUES '
    tables = ['Krwiodawcy', 'Dyskwalifikacje', 'Miasta', 'Oddzial_RCKiK', 'Pracownicy', 'Oddzial_terenowy',
              'Pobrania', 'Wyniki_badan', 'Wydania_krwi', 'Jednostki_docelowe']
    table = tables[set]

    #   Krwiodawcy
    if set == 0:
        fields = '(oddzial_rckik_id, grupy_krwi_id, imie, nazwisko, data_urodzenia, pesel, plec) '
        sqlSet = []
        for i in range(len(data)):
            sqlCommand = ins + tables[set] + " " + fields + val + "('" + data[i][0] + "', '" + data[i][1] + "', '" + \
                         data[i][2] + "', '" + data[i][3] + "', TO_DATE('" + data[i][4] + "', 'DD/MM/YYYY'), '" + \
                         data[i][5] + "', '" + data[i][6] + "')"
            sqlSet.append(sqlCommand)
        return sqlSet

    #   Dyskwalifikacje
    elif set == 1:
        fields = '(krwiodawcy_id, data, opis_przyczyn, data_koncowa) '
        sqlSet = []
        for i in range(len(data)):
            sqlCommand = ins + tables[set] + " " + fields + val + "('" + data[i][0] +\
                         "', TO_DATE('" + data[i][1] + "', 'DD/MM/YYYY'), '" + data[i][2] +\
                         "', TO_DATE('" + data[i][3] + "', 'DD/MM/YYYY'))"
            sqlSet.append(sqlCommand)
        return sqlSet

    #   Miasta
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







import cx_Oracle
import csv

username = 'SYSTEM'
password = 'SYSTEM'
database = 'localhost'

print('connection start')

Tables = ['Hotel', 'Reviewer', 'Reviews']

connection = cx_Oracle.connect(username, password, database)

cursor = connection.cursor()

try:

    for f in Tables:

        with open(f+'.csv', 'w', newline='') as CsvFile:
            cursor.execute("SELECT * FROM " + f)

            titles = []

            for row in cursor.description:
                titles.append(row[0])

            Write_to_Csv=csv.writer(CsvFile, delimiter=',')

            Write_to_Csv.writerow(titles)

            for row in cursor:
                Write_to_Csv.writerow(row)

finally:
    cursor.close()
    connection.close()
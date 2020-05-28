import cx_Oracle
from datetime import datetime
import csv

username = 'SYSTEM'
password = 'SYSTEM'
database = 'localhost'

print('connection start')

connection = cx_Oracle.connect(username, password, database)

cursor = connection.cursor()

filename="E:\Projects\BD\lb3\-third_Labarotory_DB\Hotel_Reviews.csv"

i=1

with open(filename, newline='') as file:
    CSV_Reader = csv.DictReader(file)

    try:
        for COLUMN_NAME in CSV_Reader:
            hotel_adress = COLUMN_NAME['Hotel_Address']
            hotel_name = COLUMN_NAME['Hotel_Name']
            additional_number_of_scoring = float(COLUMN_NAME['Additional_Number_of_Scoring'])
            reviewer_score = float(COLUMN_NAME['Reviewer_Score'])
            reviewer_nationality = COLUMN_NAME['Reviewer_Nationality']
            average_score = float(COLUMN_NAME['Average_Score'])
            review_date = COLUMN_NAME['Review_Date']
            positive_review= COLUMN_NAME['Positive_Review']
            negative_review= COLUMN_NAME['Negative_Review']
            total_number_of_reviews=int(COLUMN_NAME['Total_Number_of_Reviews'])

            insert = """ INSERT INTO hotel ( hotel_id, hotel_adress, hotel_name, additional_number_of_scoring)
            values (:hotel_id, :hotel_adress, :hotel_name, :additional_number_of_scoring)"""

            cursor.execute(insert, hotel_id=i, hotel_adress=hotel_adress, hotel_name=hotel_name, additional_number_of_scoring=additional_number_of_scoring)

            insert = """INSERT INTO reviewer ( reviewer_id, reviewer_score, reviewer_nationality)
            values (:reviewer_id, :reviewer_score, :reviewer_nationality)"""

            cursor.execute(insert, reviewer_id=i, reviewer_score=reviewer_score, reviewer_nationality=reviewer_nationality)

            insert = """ INSERT INTO reviews ( average_score, review_date, positive_review, negative_review, total_number_of_reviews, reviewer_id, hotel_id)
            values (:average_score, TO_DATE(:review_date,'dd/mm/yyyy'), :positive_review, :negative_review, :total_number_of_reviews,:reviewer_id,:hotel_id)"""

            cursor.execute(insert, average_score=average_score, review_date=review_date, positive_review=positive_review,negative_review=negative_review,total_number_of_reviews=total_number_of_reviews, reviewer_id=i, hotel_id=i)


            i = i + 1

    except:
        raise

connection.commit()
cursor.close()
connection.close()
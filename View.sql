CREATE OR REPLACE VIEW reviews_hotel_reviewer AS

    SELECT

        hotel.hotel_adress,
        hotel.hotel_id,
        hotel.hotel_name,
        reviews.review_date,
        reviews.average_score,
        reviewer.reviewer_score,
        reviewer.reviewer_id,
        reviewer.reviewer_nationality


    FROM
        reviews

        INNER JOIN hotel ON reviews.hotel_id = hotel.hotel_id
        INNER JOIN reviewer ON reviews.reviewer_id = reviewer.reviewer_id;
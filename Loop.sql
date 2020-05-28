DECLARE
    count_i int := 10;
BEGIN

    for i in 1..count_i LOOP

        INSERT INTO hotel ( hotel_id, hotel_adress, hotel_name, additional_number_of_scoring)
            values (i, 's Gravesandestraat 55 Oost 1092 AA Amsterdam Netherlands', 'Hotel Arena', 194 );

        INSERT INTO reviewer ( reviewer_id, reviewer_score, reviewer_nationality)
            values (i, i+1 , 'United Kingdom');

        INSERT INTO reviews ( average_score, review_date, positive_review, negative_review, total_number_of_reviews, reviewer_id, hotel_id)
            values (7.1, TO_DATE('2'||(i-1)||'/06/20'),'positive review '||i, 'negative review '||i,10, i, i);

    end loop;

END;

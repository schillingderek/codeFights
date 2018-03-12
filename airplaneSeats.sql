CREATE PROCEDURE airplaneSeats()
BEGIN

   DECLARE i,r,s,p INT;
   DECLARE d INT DEFAULT 0;

   DECLARE R CURSOR
   FOR
   SELECT * FROM requests;


   DECLARE CONTINUE HANDLER FOR NOT FOUND SET d=1;

   CREATE TABLE O LIKE seats;
   INSERT INTO O SELECT * FROM seats;

   OPEN R;

   REPEAT
      FETCH FROM R INTO i,r,s,p;
      SELECT status INTO @s FROM O WHERE seat_no = s;
      SELECT person_id INTO @p FROM O WHERE seat_no = s;
         IF (@s != 2 AND (@s = 0 OR @p = p)) THEN
            UPDATE O
            SET status = r, person_id = p
            WHERE seat_no = s; 
         END IF;
   UNTIL d END REPEAT;

   CLOSE R;

   SELECT * FROM O;
   DROP TABLE IF EXISTS O;
      
END
CREATE PROCEDURE airplaneSeats()
BEGIN
   /*initialize variables*/
   /* i,r,s,p are used to capture values from the cursor R which iterates over the table "seats"*/
   DECLARE i,r,s,p INT;
   /* d is used to stop the WHILE loop once the end of the table is reached*/
   DECLARE d INT DEFAULT 0;

   DECLARE R CURSOR
   FOR
   SELECT * FROM requests;


   DECLARE CONTINUE HANDLER FOR NOT FOUND SET d=1;

   /* make a copy of the "seats" table to modify in the WHILE loop without affecting the original db*/
   CREATE TABLE O LIKE seats;
   INSERT INTO O SELECT * FROM seats;

   OPEN R;

   REPEAT
      FETCH FROM R INTO i,r,s,p; /* iterate over the requests table*/
      SELECT status INTO @s FROM O WHERE seat_no = s;
      SELECT person_id INTO @p FROM O WHERE seat_no = s;
      /* if the seat was not already purchased and the seat was either free or reserved by the same person making the request
         update the status and person_id in the output table appropriately, otherwise ignore the request*/
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

CREATE PROCEDURE missingTransactions()
BEGIN
  /*declare a variable which will be used to store the maximum ID value in the table "transactions"*/
  DECLARE v1 INT DEFAULT 1;
  /*create a table which will list all of the numbers from 0 through the maximum ID in "transaction"*/
  DROP TABLE IF EXISTS ints;
  CREATE TABLE ints (id INT);

  /*find the max ID value in "transactions" and construct a table "ints" which contains all values from 0 through max ID*/
  SELECT MAX(id) into v1 FROM transactions;
  WHILE v1 >= 0 DO
    INSERT INTO ints (id) VALUES (v1);
    SET v1 = v1 - 1;
  END WHILE;

  /* join the "ints" and "transactions" tables and store all the places where the join produces a "NULL" in the ID
  which indicates that the ID was missing - order this list by id number*/
  SELECT ints.id as id
  FROM  ints 
  LEFT OUTER JOIN  transactions ON  ints.id =  transactions.id 
  WHERE  transactions.id IS NULL
  ORDER BY ints.id + 0;

END

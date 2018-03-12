CREATE PROCEDURE missingTransactions()
BEGIN
  DECLARE v1 INT DEFAULT 1;
  DROP TABLE IF EXISTS ints;
  CREATE TABLE ints (id INT);

  
  SELECT MAX(id) into v1 FROM transactions;
  WHILE v1 >= 0 DO
    INSERT INTO ints (id) VALUES (v1);
    SET v1 = v1 - 1;
  END WHILE;

SELECT ints.id as id
FROM  ints 
LEFT OUTER JOIN  transactions ON  ints.id =  transactions.id 
WHERE  transactions.id IS NULL
ORDER BY ints.id + 0;

END
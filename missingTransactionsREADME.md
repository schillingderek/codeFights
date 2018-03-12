You have the table missingTransactions, which describes seats on an airplane. It has the following columns:

    id - The ID of the transaction;
    amount - The transaction amount;
    name - The name of the person who made this transaction.

This table stores all your incoming transactions. But after careful examination you've noticed that some transactions are missing!

You know that the first transaction has its id set to 0, the second one has id = 1, and so on. Basically, all transactions form a continuous integer sequence from 0 to the maximum id. Now you want to find the missing transactions.

Your task is to return the ids of the missing transactions, sorted in ascending order.
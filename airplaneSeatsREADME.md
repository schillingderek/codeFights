You work for an airline, and you've been tasked with improving the procedure for reserving and buying seats.
You have the table seats, which describes seats in the airplane. It has the following columns:

    seat_no - The unique number of the seat;
    status - The status of the seat (0 indicates free, 1 indicates reserved, and 2 indicates purchased);
    person_id - The ID of the person who reserved/purchased this seat (0 if the corresponding status is 0).

You also have the table requests, which contains the following columns:

    request_id - The unique ID of the request;
    request - The description of the request (1 indicates reserve, 2 indicates purchase);
    seat_no - The number of the seat that the person want to reserve/purchase;
    person_id - The ID of the person who wants to reserve/purchase this seat.

A person can reserve/purchase a free seat and can purchase a seat that they have reserved.

Your task is to return the table seats after the given requests have been performed.

Note: requests are applied from the lowest request_id; it's guaranteed that all values of seat_no in the table requests are presented in the table seats.
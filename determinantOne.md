https://codefights.com/challenge/v3S83Tbdm54s9hAxi
Given a positive integer n, calculate the number of 2 × 2 integer matrices with determinant 1 and all entries less than or equal to n in absolute value. Return the number modulo 109 + 7.
Example
•	For n = 1, the output should be
determinantOne(n) = 20.
There are 20 2 × 2 matrices with determinant 1 and all entries less than or equal to 1 in absolute value:
[[-1, -1], [0, -1]], [[-1, -1], [1, 0]],
[[-1, 0], [-1, -1]], [[-1, 0], [0, -1]],
[[-1, 0], [1, -1]], [[-1, 1], [-1, 0]],
[[-1, 1], [0, -1]], [[0, -1], [1, -1]],
[[0, -1], [1, 0]], [[0, -1], [1, 1]],
[[0, 1], [-1, -1]], [[0, 1], [-1, 0]],
[[0, 1], [-1, 1]], [[1, -1], [0, 1]],
[[1, -1], [1, 0]], [[1, 0], [-1, 1]],
[[1, 0], [0, 1]], [[1, 0], [1, 1]],
[[1, 1], [-1, 0]], [[1, 1], [0, 1]]


You will be given a 2D matrix of English lower case letters. Your mission today is to find the longest path that following these rules below.

    The path can only be straight line or form a 90 degree corner;
    In each step, the next letter must be different from the current letter;
    The path cannot cut itself or form a loop path;
    If there are more than one longest path, pick the highest one.

Example
For

letterMap = 
a   b   c
d   e   f
g   h   i

the output should be
letterPath(letterMap) = "ihgdefcba".
In this example, we have several longest paths: abcfihgde, adghifcbe, edghifcba, etc. The highest one is the final answer ihgdefcba
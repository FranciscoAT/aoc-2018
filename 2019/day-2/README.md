# [Day 2](./src)

### [Part one](./src/part_1.py)

Runtime: 0.03s

This one made use of a tape with Intcodes. With int code of 1 and 2 meaning. Take the first integer after int code 1/2 and the second integer. Then find the values on the tape at the integer locations defined by the first and second integer. Add them if int code is 1 else multiply, then place the result at the integer location defined by the third integer after the int code. So for example:

```
Tape: 1 2 3 5 1 2 3 4
The cursor would read one then take the value at tape[2] = 3  and tape[3] = 5 and add them together, 8, then place this value at position 5.
After step 1: 1 2 3 5 1 8 3 4
```

After performing the intcode the cursor moves forward 4 places. An additional note is that if the int code found is 99 the program exits gracefully. Else if the int code found is neither 1, 2, nor 99 the program fails.

The solution in part one was to simply implement this computer, take the input and spit out the output, which is the value at tape[0]. Straightforward stuff.

### [Part two](./src/part_2.py)

Runtime: 0.29s

Part two was a little more interesting. It wanted to know the noun (value at position 1) and verb (value at position 2) such that the output of the same input would give us the value 19690720. The solution here was to brute force the value of the noun and the verb. Since any of the values can only be between 0 and 99 (as defined by the problem). We are only dealing with 10000 possible checks, which isn't bad. Therefore the solution was to just brute force it and check if we hit the correct output and return back the noun and verb and quit the program.



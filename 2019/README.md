# 2019 Advent of Code 

Merry Christmas Everyone!! Here I'll be doing a brief overview of the days challenge and my thoughts into how I solved it. Some of these will be shorter, others longer. Just depends on how I feel at the moment of writing them! 

--------

## [Day 1](./day-1)

### [Part one](./day-1/part_1.py)

Part one was pretty straight-forward. All it required was to take a series of inputs and perform a calculation on each input before adding it to a running total. Where the calcuation is as follows:

```
calculated_fuel = floor(input / 3) - 2
```

### [Part two](./day-1/part_2.py)

Part two introduces recursion. In order to calculate the correct amount of fuel for each input, we must calculate the amount of fuel needed for the calculated amount of fuel, etc.... Where the fuel calculation is the same as part one. Except recursion stops when the fuel needed is less than or equal to 0.

So for example an input fuel amount of 30 would result in the following calculation:

```
f0 = 60 (fuel needed)
f1 = floor(60 / 3) - 2 = 18
f2 = floor(8 / 3) - 2 = 4
f3 = floor(4 / 3) - 2 = -1

Therefore fuel required for 
f0 = f1 + f2 + f3 
   = (18) + (4) + (-1), but since f3 is less than 0 it becomes just 0
   = (18) + (4) + (0)
   = 22
```

## [Day 2](./day-2)

### [Part one](./day-2/part_1.py)

This one made use of a tape with Intcodes. With int code of 1 and 2 meaning. Take the first integer after int code 1/2 and the second integer. Then find the values on the tape at the integer locations defined by the first and second integer. Add them if int code is 1 else multiply, then place the result at the integer location defined by the third integer after the int code. So for example:

```
Tape: 1 2 3 5 1 2 3 4
The cursor would read one then take the value at tape[2] = 3  and tape[3] = 5 and add them together, 8, then place this value at position 5.
After step 1: 1 2 3 5 1 8 3 4
```

After performing the intcode the cursor moves forward 4 places. An additional note is that if the int code found is 99 the program exits gracefully. Else if the int code found is neither 1, 2, nor 99 the program fails.

The solution in part one was to simply implement this computer, take the input and spit out the output, which is the value at tape[0]. Straightforward stuff.

### [Part two](./day-2/part_2.py)

Part two was a little more interesting. It wanted to know the noun (value at position 1) and verb (value at position 2) such that the output of the same input would give us the value 19690720. The solution here was to brute force the value of the noun and the verb. Since any of the values can only be between 0 and 99 (as defined by the problem). We are only dealing with 10000 possible checks, which isn't bad. Therefore the solution was to just brute force it and check if we hit the correct output and return back the noun and verb and quit the program.


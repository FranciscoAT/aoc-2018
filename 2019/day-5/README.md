# [Day 5](./src)

### [Part one](./src/part_1.py)

Runtime: 0.02s

So in this one we expand on the int code computer we defined in [day 2](../day-2/). We added two need commands, command 3 which takes in an input and stores it somewhere in the int code tape. As well command 4 with outputs the value of the first parameter. However the biggest change to all this is the concept of the parameter modes. In day 2 all parameters were taken as positional. Which means that the parameter value references the position in the tape which is parameter mode 0. However now we define parameter mode 1 which is the immediate value, which is to say the value is the value of the parameter itself. These parameter modes are held in the intcode itself. Meaning the int code will now take the form of an up to 5 digit number where:

```
ABCDE
A = parameter mode for parameter 3
B = parameter mode for parameter 2
C = parameter mode for parameter 1
DE = intcode (01, 02, ..., 05, 99)

Note if not specified then we assume 0. Ex. 103 is equivalent to 00103
```

the solution I approached was rather brute force. Simply just a while loop, parse out the intcode and get the values needed to perform the coresponding operation by iterating over the parameters modes. 

### [Part two](./src/part_2.py)

Runtime: 0.02s

Expanding on the first part we here simply add a few new operations. 
- Operation 5 which checks if the first parameter is non-zero, if so it will jump to current pointer/index to the position specified by parameter 2 
- Operation 6 similar to operation 6 which does the same thing but checks if the first parameter is zero
- Operation 7 which stores 1 at the position specified by parameter 3 if the first parameter is less than the second parameter else stores 0
- Operation 8 which stores 1 at the position specified by parameter 3 if the first parameter is equal to the second parameter else stores 0

The bulk of the work was done in part one, so for this part I simply expanded it. However note that for operation 7 and 8 will always store by position and not immediate

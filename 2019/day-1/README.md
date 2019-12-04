# [Day 1](./src)

### [Part one](./src/part_1.py)

Runtime: 0.04s

Part one was pretty straight-forward. All it required was to take a series of inputs and perform a calculation on each input before adding it to a running total. Where the calcuation is as follows:

```
calculated_fuel = floor(input / 3) - 2
```

### [Part two](./src/part_2.py)

Runetime: 0.04s

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


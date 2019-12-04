# [Day 4](./src)

### [Part one](./src/part_1.py)

Todays was a fun and rather easy one. Essentially we are given a range of numbers and we need to find the "valid passwords". They are defined as follows:

- Digits must always be increasing
- There must exist two of the same number in the number

For myself the solution then was to simply iterate over every integer in the range defined. Then convert it to a str and sort the string. If the sorted string is the same as the input password then the passwords digits are always increasing. Then we created an array of strings that contain each doubles of each integer, ie. ["11", "22", "33", ...]. Then we just check if any element in this list is in the passed in password. If the above are satisfied we increment the total count.

### [Part two](./src/part_2.py)

Expanding off of part one, the second criteria gets changed. Two digits must be the same, but there must exist only two of them in a group. Which is to say, 11122 is valid since 22 eixst in a group of two and no more. However 1222 would be invalid since 2 exists in a group of more than 2 digits.

So we only have to change the function `adjcent_exists` again. We can also use the fact that the password must be ordered in an increasing fashion to our advantage. We can look to see if XX is in the password and check to see if XXX is in the password. Since it's increasing it is required that all digits of X will be adjacent. Therefore if XX exists and XXX doesn't exist then XX is in a grouping of two, and we can return true from that.

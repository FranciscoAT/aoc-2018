# [Day 7](./src)

### [Part one](./src/part_1.py)

More intcodes!!! :')

This was a fun one essentially we need to initialize 5 int code computers. Each computer will then ask for a `phase_setting` then an `input`. The computers are lined up in sequence. Such that the output from computer 1 is the `input` to computer 2, etc.... The output from computer 5 is the final output of the program. The `phase_setting` are values between 0 and 4, and each value can only be used once for each amplifier. Which is to say in one run of the program two amplifiers cannot have the same setting. The solution I approached was to simply take my solution from [day 5](../day-5) and throw it into a class with some variables for each computer so we can just throw in the tape, the previous output and the phase setting, then output the result from the last computer. Then we take this loop and iterate over every permutation of the list `[0, 1, 2, 3, 4]`.

Runtime: 0.04s

### [Part two](./src/part_2.py)

Part two was definitely a step up from Part one. Although the wording was not super great and I had to turn to [Reddit](https://www.reddit.com/r/adventofcode/comments/e7aqcb/2019_day_7_part_2_confused_with_the_question/) to get a better idea of how the program is supposed to work. Essentially we now have a feedback mode which involves phase settings from `5-9` instead of settings `0-4`. Additionally, and this is key, *if* the last computer outputs a value and does not end (which is to say hit intcode `99`), then we take this output and feed it into computer one. Additionally, each computer maintains their own index and their own version of the tape (each beginning with an index of 0 and the same initial tape from the [input](./src/day-7.in)). Then if we hit the end condition on the last computer we take the last output that that computer spat out, which is to say that generally the last output would be from the previous loop, however I just maintained the last output in the class for the int computer. Then the rest above follows, iterate over each permutation of `5-9`.

A real trick in bug fixing this was realizing that the tape was shared between each of my computers! (oops). I had to initialize with `self.tape = tape[:]` rather than `self.tape = tape`

Runtime: 0.06s

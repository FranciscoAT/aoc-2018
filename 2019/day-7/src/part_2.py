import itertools
from typing import List


class IntCodeComputer:
    def __init__(self, amp_setting: int, tape: List[int]) -> None:
        self.amp_setting = amp_setting
        self.last_output = None
        self.amp_setting_set = False
        self.tape = tape[:]
        self.end_condition_hit = False
        self.index = 0
        self.is_last_amp = False

    def run_computer(self, input_setting: int) -> int:
        while self.index < len(self.tape):
            if self.tape[self.index] < 1:
                raise Exception("Something went wrong")

            str_code = str(self.tape[self.index]).zfill(5)

            if str_code[-2:] == "01":
                first_component = (
                    self.tape[self.tape[self.index + 1]]
                    if str_code[-3] == "0"
                    else self.tape[self.index + 1]
                )
                second_component = (
                    self.tape[self.tape[self.index + 2]]
                    if str_code[-4] == "0"
                    else self.tape[self.index + 2]
                )
                sum = first_component + second_component

                if str_code[-5] == "0":
                    self.tape[self.tape[self.index + 3]] = sum
                elif str_code[-5] == "1":
                    self.tape[self.index + 3] = sum
                else:
                    raise Exception("Something went wrong")

                self.index += 4
            elif str_code[-2:] == "02":
                first_component = (
                    self.tape[self.tape[self.index + 1]]
                    if str_code[-3] == "0"
                    else self.tape[self.index + 1]
                )
                second_component = (
                    self.tape[self.tape[self.index + 2]]
                    if str_code[-4] == "0"
                    else self.tape[self.index + 2]
                )
                multiple = first_component * second_component

                if str_code[-5] == "0":
                    self.tape[self.tape[self.index + 3]] = multiple
                elif str_code[-5] == "1":
                    self.tape[self.index + 3] = multiple
                else:
                    raise Exception("Something went wrong")

                self.index += 4
            elif str_code[-2:] == "03":
                program_input = input_setting
                if self.amp_setting_set is False:
                    program_input = self.amp_setting
                    self.amp_setting_set = True
                if str_code[-3] == "0":
                    self.tape[self.tape[self.index + 1]] = program_input
                elif str_code[-3] == "1":
                    self.tape[self.index + 1] = program_input
                else:
                    raise Exception("Something went wrong")

                self.index += 2
            elif str_code[-2:] == "04":
                if str_code[-3] == "0":
                    self.last_output = self.tape[self.tape[self.index + 1]]
                elif str_code[-3] == "1":
                    self.last_output = self.tape[self.index + 1]
                else:
                    raise Exception("Something went wrong")
                self.index += 2
                # In feedback mode outputing a number "ends the program"
                break
            elif str_code[-2:] == "05":
                to_compare = (
                    self.tape[self.tape[self.index + 1]]
                    if str_code[-3] == "0"
                    else self.tape[self.index + 1]
                )
                if to_compare != 0:
                    self.index = (
                        self.tape[self.tape[self.index + 2]]
                        if str_code[-4] == "0"
                        else self.tape[self.index + 2]
                    )
                else:
                    self.index += 3
            elif str_code[-2:] == "06":
                to_compare = (
                    self.tape[self.tape[self.index + 1]]
                    if str_code[-3] == "0"
                    else self.tape[self.index + 1]
                )
                if to_compare == 0:
                    self.index = (
                        self.tape[self.tape[self.index + 2]]
                        if str_code[-4] == "0"
                        else self.tape[self.index + 2]
                    )
                else:
                    self.index += 3
            elif str_code[-2:] == "07":
                alpha = (
                    self.tape[self.tape[self.index + 1]]
                    if str_code[-3] == "0"
                    else self.tape[self.index + 1]
                )
                beta = (
                    self.tape[self.tape[self.index + 2]]
                    if str_code[-4] == "0"
                    else self.tape[self.index + 2]
                )
                self.tape[self.tape[self.index + 3]] = 1 if alpha < beta else 0
                self.index += 4
            elif str_code[-2:] == "08":
                alpha = (
                    self.tape[self.tape[self.index + 1]]
                    if str_code[-3] == "0"
                    else self.tape[self.index + 1]
                )
                beta = (
                    self.tape[self.tape[self.index + 2]]
                    if str_code[-4] == "0"
                    else self.tape[self.index + 2]
                )
                self.tape[self.tape[self.index + 3]] = 1 if alpha == beta else 0
                self.index += 4
            elif str_code[-2:] == "99":
                self.end_condition_hit = True
                break
            else:
                raise Exception("Something went wrong")

        return self.last_output


def main() -> None:
    with open("day-7.in", "r") as tape_file:
        tape = [int(x) for x in tape_file.readline().split(",")]

    amp_settings = list(itertools.permutations([5, 6, 7, 8, 9]))
    highest_signal = -1

    for amp_setting in amp_settings:
        amp_computers = []
        for index, amp in enumerate(amp_setting):
            new_amp = IntCodeComputer(amp, tape)
            if index == (len(amp_setting) - 1):
                new_amp.is_last_amp = True
            amp_computers.append(new_amp)

        current_input = 0
        current_amp = 0
        while amp_computers[-1].end_condition_hit is False:
            current_input = amp_computers[current_amp].run_computer(current_input)
            current_amp = (current_amp + 1) % 5

        if amp_computers[-1].last_output > highest_signal:
            highest_signal = amp_computers[-1].last_output

    print(highest_signal)


if __name__ == "__main__":
    main()

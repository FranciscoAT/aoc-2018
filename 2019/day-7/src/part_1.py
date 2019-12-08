import itertools
from typing import List


class IntCodeComputer:
    def __init__(self, amp_setting: int, input_setting: int) -> None:
        self.amp_setting = amp_setting
        self.input_setting = input_setting
        self.last_output = None
        self.amp_setting_set = False

    def run_computer(self, tape: List[int]) -> int:
        index = 0
        while index < len(tape):
            if tape[index] < 1:
                raise Exception("Something went wrong")

            str_code = str(tape[index]).zfill(5)

            if str_code[-2:] == "01":
                first_component = (
                    tape[tape[index + 1]] if str_code[-3] == "0" else tape[index + 1]
                )
                second_component = (
                    tape[tape[index + 2]] if str_code[-4] == "0" else tape[index + 2]
                )
                sum = first_component + second_component

                if str_code[-5] == "0":
                    tape[tape[index + 3]] = sum
                elif str_code[-5] == "1":
                    tape[index + 3] = sum
                else:
                    raise Exception("Something went wrong")

                index += 4
            elif str_code[-2:] == "02":
                first_component = (
                    tape[tape[index + 1]] if str_code[-3] == "0" else tape[index + 1]
                )
                second_component = (
                    tape[tape[index + 2]] if str_code[-4] == "0" else tape[index + 2]
                )
                multiple = first_component * second_component

                if str_code[-5] == "0":
                    tape[tape[index + 3]] = multiple
                elif str_code[-5] == "1":
                    tape[index + 3] = multiple
                else:
                    raise Exception("Something went wrong")

                index += 4
            elif str_code[-2:] == "03":
                program_input = self.input_setting
                if self.amp_setting_set is False:
                    program_input = self.amp_setting
                    self.amp_setting_set = True
                if str_code[-3] == "0":
                    tape[tape[index + 1]] = program_input
                elif str_code[-3] == "1":
                    tape[index + 1] = program_input
                else:
                    raise Exception("Something went wrong")

                index += 2
            elif str_code[-2:] == "04":
                if str_code[-3] == "0":
                    self.last_output = tape[tape[index + 1]]
                elif str_code[-3] == "1":
                    self.last_output = tape[index + 1]
                else:
                    raise Exception("Something went wrong")

                index += 2
            elif str_code[-2:] == "05":
                to_compare = (
                    tape[tape[index + 1]] if str_code[-3] == "0" else tape[index + 1]
                )
                if to_compare != 0:
                    index = (
                        tape[tape[index + 2]]
                        if str_code[-4] == "0"
                        else tape[index + 2]
                    )
                else:
                    index += 3
            elif str_code[-2:] == "06":
                to_compare = (
                    tape[tape[index + 1]] if str_code[-3] == "0" else tape[index + 1]
                )
                if to_compare == 0:
                    index = (
                        tape[tape[index + 2]]
                        if str_code[-4] == "0"
                        else tape[index + 2]
                    )
                else:
                    index += 3
            elif str_code[-2:] == "07":
                alpha = (
                    tape[tape[index + 1]] if str_code[-3] == "0" else tape[index + 1]
                )
                beta = tape[tape[index + 2]] if str_code[-4] == "0" else tape[index + 2]
                tape[tape[index + 3]] = 1 if alpha < beta else 0
                index += 4
            elif str_code[-2:] == "08":
                alpha = (
                    tape[tape[index + 1]] if str_code[-3] == "0" else tape[index + 1]
                )
                beta = tape[tape[index + 2]] if str_code[-4] == "0" else tape[index + 2]
                tape[tape[index + 3]] = 1 if alpha == beta else 0
                index += 4
            elif str_code[-2:] == "99":
                break
            else:
                raise Exception("Sometihng went wrong")

        return self.last_output


def main() -> None:
    with open("day-7.in", "r") as tape_file:
        tape = [int(x) for x in tape_file.readline().split(",")]

    amp_settings = list(itertools.permutations([0, 1, 2, 3, 4]))
    highest_signal = -1

    for amp_setting in amp_settings:
        current_input = 0
        for amp in amp_setting:
            current_input = IntCodeComputer(amp, current_input).run_computer(tape)
        if current_input > highest_signal:
            highest_signal = current_input

    print(highest_signal)


if __name__ == "__main__":
    main()

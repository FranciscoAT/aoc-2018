from typing import List


def main() -> None:
    program_input = 1

    with open("day-5.in", "r") as tape_file:
        tape = [int(x) for x in tape_file.readline().split(",")]

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
                raise Exception("something went wrong")

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
                raise Exception("something went wrong")

            index += 4
        elif str_code[-2:] == "03":
            if str_code[-3] == "0":
                tape[tape[index + 1]] = program_input
            elif str_code[-3] == "1":
                tape[index + 1] = program_input
            else:
                raise Exception("something went wrong")

            index += 2
        elif str_code[-2:] == "04":
            if str_code[-3] == "0":
                print(tape[tape[index + 1]])
            elif str_code[-3] == "1":
                print(tape[index + 1])
            else:
                raise Exception("something went wrong")

            index += 2
        elif str_code[-2:] == "99":
            print("Ending program...")
            break


if __name__ == "__main__":
    main()

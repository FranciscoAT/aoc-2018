def calculate(noun: int, verb: int) -> bool:
    print(f"Trying {noun} {verb}")
    tape = []
    with open("day-2.in", "r") as int_code_file:
        tape = [int(x) for x in int_code_file.readline().split(",")]

    tape[1] = noun
    tape[2] = verb

    for i in range(0, len(tape), 4):
        if tape[i] == 99:
            break

        if tape[i] == 1:
            tape[tape[i + 3]] = tape[tape[i + 1]] + tape[tape[i + 2]]
        elif tape[i] == 2:
            tape[tape[i + 3]] = tape[tape[i + 1]] * tape[tape[i + 2]]
        else:
            raise Exception(f"Something went wrong: {tape[i]}")

    print(tape[0])
    if tape[0] == 19690720:
        print(f"Found the solution. Noun: {noun}, Verb: {verb}")
        print(tape)
        return True

    return False


def main() -> None:
    for noun in range(0, 99):
        for verb in range(0, 99):
            success = calculate(noun, verb)
            if success:
                return


if __name__ == "__main__":
    main()

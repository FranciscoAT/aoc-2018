def main() -> None:
    tape = []
    with open("day-2.in", "r") as int_code_file:
        tape = [int(x) for x in int_code_file.readline().split(",")]

    for i in range(0, len(tape), 4):
        if tape[i] == 99:
            break

        if tape[i] == 1:
            tape[tape[i + 3]] = tape[tape[i + 1]] + tape[tape[i + 2]]
        elif tape[i] == 2:
            tape[tape[i + 3]] = tape[tape[i + 1]] * tape[tape[i + 2]]
        else:
            print(f"Something went wrong: {tape[i]}")

    print(tape)


if __name__ == "__main__":
    main()

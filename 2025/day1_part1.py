DIAL_SIZE = 100
START_POSITION = 50
INPUT_FILE = "inputs/day1_inputs.txt"


def solve_safe_password(file_path: str) -> int:
    with open(file_path, "r") as file:
        password_count = 0
        dial_number = START_POSITION

        for line in file:
            line = line.strip()
            value = int(line[1:])
            if line.startswith("L"):
                value = -value
            dial_number = (dial_number + value) % DIAL_SIZE
            if dial_number == 0:
                password_count += 1

        return password_count


if __name__ == "__main__":
    password = solve_safe_password(INPUT_FILE)
    print(f"PASSWORD: {password}")

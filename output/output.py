from datetime import datetime

def print_output(lines):
    filename = datetime.now().strftime("scan_%Y-%m-%d_%H-%M-%S.txt")
    with open(filename, "w") as file:
        file.write(f"File created at: {datetime.now()}\n")
        for line in lines:
            file.write(f"{line}\n")
from datetime import datetime

def print_output(lines):
    with open("datetime.now()", "w") as file:
        file.write(f"File created at: {datetime.now()}\n")
        for line in lines:
            file.write(line)
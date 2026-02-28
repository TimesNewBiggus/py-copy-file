from pathlib import Path


def copy_file(command: str) -> None:

    if (len(command.split()) == 3
            and command.split()[0] == "cp"
            and Path(command.split()[1]).exists()
            and command.split()[1] != command.split()[2]):

        with (open(command.split()[1], "r") as original_file,
              open(command.split()[2], "a") as copied_file):

            for line in original_file:
                copied_file.write(line)

from pathlib import Path


def setup():
    count = 0
    directory = str(Path.cwd()) + "/Unmerged/"
    for path in Path(directory).iterdir():
        if path.is_file():
            count += 1
    Number = count - 1
    Spreadsheets = [""] * Number

    i = 0
    for paths in Path(directory).iterdir():
        if paths.name != ".DS_Store" and paths.name != "._.DS_Store" and paths.name != "unmerged.txt":
            if paths.is_file():
                Spreadsheets[i] = paths.name
                i += 1
    return Spreadsheets, directory

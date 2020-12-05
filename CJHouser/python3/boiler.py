from typing import List

def getLines(filename: str) -> List[str]:
    """Return a list containing the lines of a file without newline characters."""
    with open("../inputs/" + filename, 'r') as fd: 
        lines = fd.readlines()
    return [l.strip() for l in lines]

def fileContents(filename: str) -> str:
    """Return the raw file contents."""
    with open("../inputs/" + filename, 'r') as fd:
        contents = fd.read()
    return contents

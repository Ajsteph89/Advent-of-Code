import sys
from pathlib import Path












if __name__ == "__main__":
    file = Path(sys.argv[1])
    if Path.is_file(file):
        get_position(Path.read_text(file))
    else:
        raise TypeError("This is not a file")
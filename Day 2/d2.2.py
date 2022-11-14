import sys
from pathlib import Path

def get_position(input):
    depth = 0
    horizontal = 0 
    aim = 0 
    data = input.split()
    d = [(data[i], data[i+1]) for i in range(0, len(data), 2)]
    for x in d:
        num = eval(x[1])
        if x[0] == 'forward':
            horizontal += num
            depth += (aim * num)
        if x[0] == 'up':
            aim -= num
        if x[0] == 'down':
            aim += num

    print ('Horizontal distance:', horizontal)
    print ('Vertical depth:', depth)
    print('Multiplied:', horizontal * depth)


if __name__ == "__main__":
    file = Path(sys.argv[1])
    if Path.is_file(file):
        get_position(Path.read_text(file))
    else:
        raise TypeError("This is not a file")
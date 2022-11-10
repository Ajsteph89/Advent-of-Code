import sys
from pathlib import Path


def depth_increases(input):
    data = (input.split())
    nums = [eval(i) for i in data]
    count = 0
    for i in range(1, len(nums)):
        if nums[i - 1] < nums[i]:
            count += 1
    print(count)


if __name__ == "__main__":
    file = Path(sys.argv[1])
    if Path.is_file(file):
        depth_increases(Path.read_text(file))
    else:
        raise TypeError("This is not a file")

import sys
from pathlib import Path


def three_depth_increases(input):
    data = (input.split())
    nums = [eval(i) for i in data]
    count = 0
    window_size = 3
    for i in range(len(nums) - window_size + 1):
        if (sum(nums[i: i + window_size])) < (sum(nums[(i+1): i + window_size + 1])):
            count += 1
    print(count)



if __name__ == "__main__":
    file = Path(sys.argv[1])
    if Path.is_file(file):
        three_depth_increases(Path.read_text(file))
    else:
        raise TypeError("This is not a file")














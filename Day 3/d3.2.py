import sys
from pathlib import Path



def diagnostics(input):
    nums = input.split()
    for col in range(len(nums[0])):
        filter_ones = []
        filter_zeros = []
        ones = 0
        zeros = 0
        for row in range(len(nums)):
            if nums[row][col] == '1':
                filter_ones.append(nums[row])
                ones += 1
            if nums[row][col] == '0':
                filter_zeros.append(nums[row])
                zeros += 1
        print(ones, zeros)
        if len(filter_ones) >= len(filter_zeros):
            nums = filter_ones
        if len(filter_ones) < len(filter_zeros):
            nums = filter_zeros
        print(nums)




if __name__ == "__main__":
    file = Path(sys.argv[1])
    if Path.is_file(file):
        diagnostics(Path.read_text(file))
    else:
        raise TypeError("This is not a file")
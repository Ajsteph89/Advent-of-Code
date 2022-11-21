import sys
from pathlib import Path



def diagnostics(input):
    nums = input.split()
    
    oxygen = get_oxygen(nums)
    co2 = get_cohtwo(nums)

    oxygen_binary = ''.join(map(str, oxygen)) 
    co2_binary = ''.join(map(str, co2)) 

    oxygen_decimal = get_decimal(oxygen_binary)
    co2_decimal = get_decimal(co2_binary)

    life_support = oxygen_decimal * co2_decimal
    
    print('Oxygen is:', oxygen_decimal)
    print('CO2 is:', co2_decimal)
    print('Life Support is:', life_support)

def get_oxygen(nums):
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
            if len(filter_ones) >= len(filter_zeros):
                nums = filter_ones
            if len(filter_ones) < len(filter_zeros):
                nums = filter_zeros
            if len(nums) == 1:
                return(nums)

def get_cohtwo(nums):
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
            if len(filter_ones) >= len(filter_zeros):
                nums = filter_zeros
            if len(filter_ones) < len(filter_zeros):
                nums = filter_ones
            if len(nums) == 1:
                return(nums)

def get_decimal(binary):
    decimal = int(binary, 2)
    return(decimal)


if __name__ == "__main__":
    file = Path(sys.argv[1])
    if Path.is_file(file):
        diagnostics(Path.read_text(file))
    else:
        raise TypeError("This is not a file")
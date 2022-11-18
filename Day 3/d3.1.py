import sys
from pathlib import Path



def diagnostics(input):
    nums = input.split()
    gamma = []
    epsilon = []
    for col in range(len(nums[0])):
        ones = 0
        zeros = 0
        for row in range(len(nums)):
            if nums[row][col] == '1':
                ones += 1
            if nums[row][col] == '0':
                zeros += 1
        get_gamma(ones, zeros, gamma)
        get_epsilon(ones, zeros, epsilon)

    # take lists and turn them into a string
    gamma_binary = ''.join(map(str, gamma)) 
    epsilon_binary = ''.join(map(str, epsilon)) 
    
    #convert binary string to decimal
    gamma_decimal = get_decimal(gamma_binary)
    epsilon_decimal = get_decimal(epsilon_binary)
    
    print('Gamma is:', gamma_decimal)
    print('Epsilon is:', epsilon_decimal)
    print('Power consumption is:', (gamma_decimal * epsilon_decimal))

#creates new list of most common ones and zeros 
def get_gamma(ones, zeros, gamma):
    if ones > zeros:
        gamma.append(1)
    if zeros > ones:
        gamma.append(0)
    return(gamma)

#creates new list of least common ones and zeros
def get_epsilon(ones, zeros, epsilon):
    if ones > zeros:
        epsilon.append(0)
    if zeros > ones:
        epsilon.append(1)
    return(epsilon)

# converts binary string to decimal number
def get_decimal(binary):
    decimal = int(binary, 2)
    return(decimal)


if __name__ == "__main__":
    file = Path(sys.argv[1])
    if Path.is_file(file):
        diagnostics(Path.read_text(file))
    else:
        raise TypeError("This is not a file")
letters = 'abcdefghijklmnopqrstuvwxyz'

def generate_combinations(string, length):

    if length == 0:
        return [string]
    else:
        combinations = []
        for letter in letters:
            combinations += generate_combinations(string + letter, length - 1)
        return combinations


if __name__ == "__main__":
# Specify the length
    length = 4


    combinations = generate_combinations("", length)

    # Print combinations
    for combination in combinations:
        print(combination)
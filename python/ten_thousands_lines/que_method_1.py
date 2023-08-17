## start from 0 lines of code to 10,000

letters = 'abcdefghijklmnopqrstuvwxyz'

def generate_combinations(length):
    # Start with all the letters in the queue
    combinations = list(letters)
    
    while len(combinations[0]) < length:
        # Take the first combination off the front of the queue
        combination = combinations.pop(0)
        
        # Add a new letter onto the end of this combination and add it back into the queue
        for letter in letters:
            combinations.append(combination + letter)
            
    return combinations


if __name__ == "__main__":
    # Specify the length
    length = 4

    combinations = generate_combinations(length)

    # Print combinations
    for combination in combinations:
        print(combination)
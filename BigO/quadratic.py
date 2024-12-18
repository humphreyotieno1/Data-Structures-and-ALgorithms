# finding the possible combinations from two dice rolled together with same number of sides
# function to find the possible combinations
def find_combinations(sides):
    combinations = []
    
    for i in range(1, sides + 1):
        for j in range(1, sides + 1):
            combinations.append((i, j))
            
    return combinations

print(find_combinations(6))

# possible combinations for dice with different number of sides
def find_diff_combinations(sides1, sides2):
    combinations = []
    
    for i in range(1, sides1 + 1):
        for j in range(1, sides2 + 1):
            combinations.append((i, j))
            
    return combinations

print(find_diff_combinations(6, 8))
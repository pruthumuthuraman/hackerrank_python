# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product

def solve():
    # Read K and M
    k, m = map(int, input().split())
    
    # Read each list, squaring the elements immediately
    lists = []
    for _ in range(k):
        # row[0] is the size 'n', row[1:] are the actual elements
        row = list(map(int, input().split()))
        squared_elements = [x**2 for x in row[1:]]
        lists.append(squared_elements)
    
    # Generate all possible combinations picking one from each list
    max_val = 0
    for combination in product(*lists):
        # Calculate sum of squares modulo M
        current_sum = sum(combination) % m
        if current_sum > max_val:
            max_val = current_sum
            
    print(max_val)

if __name__ == "__main__":
    solve()

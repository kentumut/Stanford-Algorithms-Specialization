class TwoSumSolver:
    def __init__(self, filename):
        self.integers = self.read_integers_from_file(filename)  # Set to store integers
        self.valid_targets = set()  # Another set to keep track of valid target sums
    
    def read_integers_from_file(self, filename):
        with open(filename, 'r') as file:
            return set(int(line.strip()) for line in file)
    
    def find_valid_sums(self):
        for x in self.integers:
            for t in range(-10000, 10001):
                y = t - x
                if y in self.integers and y != x:
                    self.valid_targets.add(t)
        return len(self.valid_targets)

# Example usage
filename = '2sum.txt'
solver = TwoSumSolver(filename)
result = solver.find_valid_sums()
print(result)

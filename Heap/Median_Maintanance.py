def sum_of_medians_mod(numbers):
    min_heap = MinHeap()  # upper_half
    max_heap = MinHeap()  # lower_half
    med_sum = 0
    MOD = 10000

    for num in numbers:
        if len(max_heap) == 0 or num <= -max_heap.peek():
            max_heap.insert(-num)
        else:
            min_heap.insert(num)

        # Balance the heaps
        if len(max_heap) > len(min_heap) + 1:
            min_heap.insert(-max_heap.delete_min())
        elif len(min_heap) > len(max_heap):
            max_heap.insert(-min_heap.delete_min())
        
        # Calculate median
        if len(max_heap) >= len(min_heap):
            median = -max_heap.peek()
        else:
            median = min_heap.peek()
        
        med_sum = (med_sum + median) % MOD
    
    return med_sum

class MinHeap:
    def __init__(self):
        self.heap = []
    
    def insert(self, element):
        self.heap.append(element)
        self.heapify_up(len(self.heap) - 1)

    def heapify_up(self, index):
        parent_index = (index - 1) // 2
        if index > 0 and self.heap[index] < self.heap[parent_index]:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            self.heapify_up(parent_index)

    def delete_min(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heapify_down(0)
        return root
    
    def heapify_down(self, index):
        smallest = index
        left_child_index = 2 * index + 1
        right_child_index = 2 * index + 2

        if left_child_index < len(self.heap) and self.heap[left_child_index] < self.heap[smallest]:
            smallest = left_child_index
        if right_child_index < len(self.heap) and self.heap[right_child_index] < self.heap[smallest]:
            smallest = right_child_index
        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self.heapify_down(smallest)

    def peek(self):
        if len(self.heap) == 0:
            return None
        return self.heap[0]

    def __len__(self):
        return len(self.heap)

# Example usage:
numbers = []
with open("Median.txt", "r") as file:
    for line in file:
        numbers.append(int(line))

print(sum_of_medians_mod(numbers))

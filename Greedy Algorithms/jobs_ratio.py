import heapq

class Job:
    def __init__(self, weight, length, index):
        self.weight = weight
        self.length = length
        self.index = index

    def __repr__(self):
        return f"Job(weight={self.weight}, length={self.length}, index={self.index})"

def schedule_jobs(jobs):
    max_heap = [(-job.weight / job.length, -job.weight, job.index, job) for job in jobs]
    heapq.heapify(max_heap)
    return [heapq.heappop(max_heap)[3] for _ in range(len(max_heap))]

# Example usage
with open("jobs.txt") as file:
    next(file)
    jobs = [Job(int(parts[0]), int(parts[1]), i) for i, parts in enumerate(line.split() for line in file)]

scheduled_jobs = schedule_jobs(jobs)
completion_time = sum = 0
for job in scheduled_jobs:
    completion_time += job.length
    sum += completion_time * job.weight

print(sum)

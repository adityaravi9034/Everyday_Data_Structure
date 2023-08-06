"""You are given a list of tasks represented by their durations. Each task takes a specific amount of time to complete.
Your task is to schedule these tasks on different machines in such a way that each machine handles exactly two tasks,
and the difference in the total time taken by the two machines is minimized.

Write a function minimize_task_difference(tasks) that takes the list of task durations as input and returns the minimum difference 
in the total time taken by the two machines.

tasks = [2, 5, 7, 3, 1, 8, 4]

result = minimize_task_difference(tasks)
print(result)  # Output: 1

In the given example, one possible way to schedule the tasks on two machines would be as follows:

Machine 1: [2, 5, 7] (Total time: 2 + 5 + 7 = 14)
Machine 2: [3, 1, 8, 4] (Total time: 3 + 1 + 8 + 4 = 16)
The difference in the total time taken by the two machines is |14 - 16| = 2. However, there is a better way to schedule the tasks, as follows:

Machine 1: [2, 8] (Total time: 2 + 8 = 10)
Machine 2: [5, 7, 3, 1, 4] (Total time: 5 + 7 + 3 + 1 + 4 = 20)
Now, the difference in the total time taken by the two machines is |10 - 20| = 10, which is larger than the previous case.

The function should return the minimum difference, which is 1 in this example.
"""

def minimize_task_difference(tasks):
    tasks.sort()
    min_difference = float('inf')

    left, right = 0, len(tasks) - 1
    while left < right:
        difference = tasks[right] + tasks[left]
        min_difference = min(min_difference, abs(difference))

        if difference < 0:
            left += 1
        else:
            right -= 1

    return min_difference

# Example usage:
tasks = [2, 5, 7, 3, 1, 8, 4]
result = minimize_task_difference(tasks)
print(result)  # Output: 1

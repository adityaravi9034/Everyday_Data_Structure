"""You are given a list of strings, where each string represents a log entry of a system. Each log entry consists of an alphanumeric identifier (with no spaces),
followed by a colon, and then a space-separated string. The alphanumeric identifier is either a letter-logs or a digit-log.

You need to sort the logs so that all of the letter-logs come before any digit-log. The letter-logs are ordered lexicographically. 
If two letter-logs have the same content, sort them lexicographically based on their identifiers. The digit-logs should be sorted in their original order.

Write a function sort_logs(logs) that takes the list of log entries as input and returns a list of the sorted log entries.:::

Example
logs = [
    "a1: alpha",
    "b1: beta",
    "a2: gamma",
    "b2: delta",
    "1: epsilon",
    "2: zeta"
]

sorted_logs = sort_logs(logs)
print(sorted_logs)

Expected Output:

[    "a1: alpha",    "b1: beta",    "a2: gamma",    "b2: delta",    "1: epsilon",    "2: zeta"]

"""

def sort_logs(logs):
    def custom_sort_key(log):
        identifier, content = log.split(":", 1)
        if content[0].isalpha():
            return (0, content, identifier)
        return (1,)

    return sorted(logs, key=custom_sort_key)

# Example usage:
logs = [
    "a1: alpha",
    "b1: beta",
    "a2: gamma",
    "b2: delta",
    "1: epsilon",
    "2: zeta"
]

sorted_logs = sort_logs(logs)
print(sorted_logs)

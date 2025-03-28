# count primitive operations
def count_operations(n):
    count = 1
    for i in range(n):
        for j in range(n):
            count += 1
    for i in range(n):
        count += 1
    return count

# call function
operations = count_operations(5)
print(operations)

# output = 31: 5**2 + 5 + 1
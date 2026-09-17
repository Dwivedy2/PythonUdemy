# Q1
numbers = [10, 20, 30, 40, 50]
print(f"first element: {numbers[0]}")
print(f"last element: {numbers[-1]}") 
print(f"last element: {numbers[len(numbers) - 1]}")
print(f"length: {len(numbers)}")

# Q2
numbers = [10, 20, 30]
numbers.insert(1, 100)
numbers.append(40)
print(f"new numbers: {numbers}")

# Q3
def find_sum(arr):
    total = 0
    for n in arr:
        total += n
    return total

print(find_sum([1, 2, 3, 4, 5]))

# Q4
def find_max(arr):  
    mx = arr[0]
    for n in arr:
        if n > mx:
            mx = n
    return mx
        
print(find_max([4, 9, 2, 7, 1]))
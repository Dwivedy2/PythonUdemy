# Q1 — Return, don't print
def square(num):
    return num * num

res = square(5)
# print(res)

# Q2 — Maximum of 3 numbers
def find_max(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        return num1
    elif num2 > num3:
        return num2
    return num3

# print(find_max(10, 25, 15))
# print(find_max(100, 20, 30))
# print(find_max(100, 20, 300))

# Q3 — Count from 1 to N
def print_numbers(n):
    for i in range(1, n+1):
        print(i)

# print_numbers(5)

def is_even(number):
    return number % 2 == 0

print(is_even(10))
print(is_even(7))
# print(1)
# print(2)
# print(3)
# print(4)
# print(5)
# print(6)
# print(7)
# print(8)
# print(9)
# print(10)

# 1. Print 1 to 20
# for i in range(1, 21):
#     print(i)

# 2. Print even numbers from 1 to 20
# for i in range(2, 21, 2):
#     print(i)

# 3. Calculate the sum from 1 to 10
# sum = 0
# for i in range(1, 11):
#     sum += i
# print(sum)

# while loops
# Q1. Print 10 to 1 using while
i = 10
while(i >= 1):
    print(i)
    i -= 1

# Q2. Print multiples of 3 from 1 to 30 using continue
i = 0
while i < 31:
    i += 1
    if i%3 != 0:
        continue
    else:
        print(i)

# Q3. Find the first number divisible by both 7 and 11
i = 1
while True:
    if i % 7 == 0 and i % 11 == 0:
        print(i)
        break
    i += 1

# Q4. Count down from 5
i = 5
while i > 0:
    print(i)
    i -= 1
print("Lift off 🚀")
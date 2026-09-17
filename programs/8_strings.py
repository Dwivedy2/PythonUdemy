# Q1 — Indexing
s = "Programming"
print(s[0])
print(s[3])

# Q2 — Reverse
def reverse_string(s):
    return s[::-1]

print(reverse_string("hello"))

# Q3 — Count vowels ⭐
def count_vowels(s):
    s = s.lower()
    count = 0
    for ch in s:
        # if(ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u'):
        if ch in "aeiou":
            count += 1
    return count

print(count_vowels("programming"))

# Q4 — Palindrome ⭐
def is_palindrome(s):
    return s == s[::-1]

print(is_palindrome("madam"))
print(is_palindrome("hello"))
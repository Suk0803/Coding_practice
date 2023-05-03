s = input()

def is_palindrome(s):
    return s == s[::-1]

if is_palindrome(s):
    print(1)
else:
    print(0)

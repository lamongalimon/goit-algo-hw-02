from collections import deque



def check_palindrome(string):
    d = deque()
    for char in string:
        if char.isalnum():
            d.append(char.lower())
    while len(d) > 1:
        if d.popleft() != d.pop():
            print("Рядок не є паліндромом")
            return False
    print("Рядок є паліндромом")
    return True

check_palindrome("racecar")
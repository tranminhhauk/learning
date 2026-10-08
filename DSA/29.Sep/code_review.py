# 1. Reverse a string without using built-in reverse functions.
def reverse_str(strs):
    char = list(strs)
    left = 0
    right = len(char) - 1
    while left < right:
        char[left], char[right] = char[right], char[left]
        left += 1
        right -= 1
    return "".join(char)
print(reverse_str("hello"))

# 2. Find the maximum value in an array without using built-in sort/max.

def fine_max(arr):
    valMax = arr[0]
    for i in arr:
        if i > valMax:
            valMax = i
    return valMax
print(fine_max([1,2,4,6,3,54]))

# 3. Check if a string is a palindrome. E.g: “level”, “kayak”, “radar”, “deified”

def check_palindrome(s):
    ls = list(s)
    left = 0
    right = len(s)-1
    while left < right:
        if ls[left] !=ls[right]:
            return False
        else:
            left += 1
            right -=1
    return True
print(check_palindrome("kayak"))
# 4. Remove duplicates from an array.

def remove_duplicate(arr):
    result = []
    for i in arr:
        if i not in result:
            result.append(i)
    return result
print(remove_duplicate([1,2,1,2,3,4]))

# 5. FizzBuzz: Print numbers 1-100, replace multiples of 3 with “Fizz”, 5 with “Buzz”, both with “FizzBuzz”

def FizzBuzz():
    for i in range(0, 101):
        if i % 3 == 0 and i % 5 == 0:
            print('FizzBuzz')
        elif i % 3 == 0:
            print('Fizz')
        elif  i % 5 == 0:
            print('Buzz')
        else:
            print(i)
FizzBuzz()

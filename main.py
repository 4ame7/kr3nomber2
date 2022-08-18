def palindrome(string):
    string = string.lower()
    return string == string[:: -1]

s = input()
print(palindrome(s))
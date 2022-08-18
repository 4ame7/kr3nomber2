def palindrome(s):
    return s[::-1] == s
while True:
    s = input("Введите слово: ")
    print(f"{s} Это палиндром!" if palindrome(s) else "Это не палиндром")
    break
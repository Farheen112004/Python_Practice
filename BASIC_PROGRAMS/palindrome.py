def Palindrome(p):
    return p == p[::-1]
a = input()
if Palindrome(a):
    print("yes its palindrome")
else:
    print("noooooo")
    
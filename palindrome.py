a=int(input("Enter the no"))
b=a
rev=0
print(b)
while b>0:
    r=b%10
    rev=rev*10+r
    b=b//10
if rev==a:
    print("Palindrome no")
else:
    print("Not palindrome no")


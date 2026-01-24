n=int(input("Enter a number : "))
print("Even numbers : ")

count=0
i=1
while i<=n:
    if i%2==0:
        print(i)
        count=count+1
    i=i+1
print("Total even numbers : ", count)

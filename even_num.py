#Sum of Even Numbers

i = int(input("Enter Maximum Value:"))
sum=0

for num in range(1, i+1):
    if(num%2==0):
        print("{0}".format(num))
        sum=sum+num

print("Sum of even Numbers {0}={1}".format(num,sum))
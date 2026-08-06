#program to find even and odd numbers

li=[2,3,4,5,6,7,10]
even=0
odd=0
for i in li:
    if i%2==0:
        even=even+1

    else:
        odd=odd+1

print("total no.of even numbers are= ",even)
print("total no.of odd numbers are= ",odd)

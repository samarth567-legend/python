#program to find the negative elements

li=[1,2,-1,3,-2]
counter=0
for ele in li:
    if ele<1:
        counter=counter+1
print('total number of neagative elements are= ',counter)        
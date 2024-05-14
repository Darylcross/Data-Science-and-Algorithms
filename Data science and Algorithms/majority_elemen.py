#find majority element 
myList=[2,3,4,1,1,1,1,1,5]
def findMajority():
    numbers={}
    result=0
    maxNumber=0
    
    for num in myList:
        numbers[num]=1+numbers.get(num,0)
        if numbers[num]>maxNumber:
            result=num
        maxNumber=max(maxNumber,numbers[num])
    return result
    
print(findMajority())
def singleNumber(x):
    result = 0
    for num in x:
        result = num ^ result
    return result

print(singleNumber([1, 2, 3, 1, 2]))

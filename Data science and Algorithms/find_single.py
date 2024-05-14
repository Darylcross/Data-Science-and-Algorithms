# #boş olmayan bir liste veriyor bu listede bir eleman harici hepsi iki kere kullanılmış o tek elemanı bulmamızı istiyor zaman on space o1 
# liste=[1,2,3,1,2,3,4] # 4 ü bulmam gerekiyor
# new_list=[]
# new_list.append(liste[0])
# print(new_list)

# bu sorunun çözümünü xor kapısı kullanarak yazıyoruz

# def singleNumber(x):
#     result=0
#     for num in list:
#         result=num^result #burada xor kapısı kullandık
#     return result
# singleNumber([1,2,3,1,2])

def singleNumber(x):
    result = 0
    for num in x:
        result = num ^ result
    return result

print(singleNumber([1, 2, 3, 1, 2]))

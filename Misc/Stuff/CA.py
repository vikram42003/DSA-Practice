# CA Question - Write three functions in a code with same list and tuple
# 1) Filter Even Numbers from a Tuple and Return as List
# 2) Find Top N Largest Values from a List and Retum as Tuple
# 3) Replace Negative Numbers in a Tuple with Zero and Return as List

tuple1 = (1, 2, 3, 4, 5, 6, 7)
list1 = [7, 6, 5, 4, 3, 2, 1]

def filterEvenNumbers(tuple1):
    even = []
    for n in tuple1:
        if n % 2 == 0:
            even.append(n)
    return even

even = filterEvenNumbers(tuple1)
print(even)



def nLargestValues(list1, n):
    list1.sort(reverse=True)
    values = list1[:n]
    return tuple(values)

nValues = nLargestValues(list1, 3)
print(nValues)



tuple2 = (1, 3, -5, -9, 20, -1)
def replaceNegative(tuple2):
    list2 = []
    for n in tuple2:
        if n < 0:
            list2.append(0)
        else:
            list2.append(n)
    return list2

ans = replaceNegative(tuple2)
print(ans)
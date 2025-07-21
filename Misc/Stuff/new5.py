def createList():
    return [1, 2, 3, 4, 5]

def deleteElement(arr, element):
    updated = arr
    updated.remove(element)
    return updated
    
arr = createList()
print(arr)
arr = deleteElement(arr, 5)
print(arr)


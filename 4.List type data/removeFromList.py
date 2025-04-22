# remove item from list

#remove
#pop
#del
#clear

testList = ["python", "java", "c++", "c#", "javascript", "typescript"]

print(f"Removing elements in a list1 : {testList}")

testList.remove('java')

print(f"Removing by remove : {testList}")

testList.pop(2)
print(f"Removing by pop : {testList}")

testList.pop()
print(f"Removing by pop without index : {testList}")

del testList[1]
print(f"Removing by del : {testList}")

testList.clear()
print(f"Removing by clear : {testList}")
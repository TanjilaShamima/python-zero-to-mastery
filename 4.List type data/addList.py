# Add item in list

#append
# insert
# extend

testList = ["python", "java", "c++", "c#", "javascript", "typescript"]

print(f"1. Adding elements in a list1 : {testList}")

testList.append("new thing")

print(f"2. Adding elements in a list2: {testList}")

testList.insert(2, "new thing 2")

print(f"3. Adding elements in a list3: {testList}")

testList.extend(["new thing 3", "new thing 4"])

print(f"4. Adding elements in a list4: {testList}")

testList.append(5)
print(f"5. Adding elements in a list: {testList}")

testList.append(True)

print(f"6. Adding elements in a list5: {testList}")

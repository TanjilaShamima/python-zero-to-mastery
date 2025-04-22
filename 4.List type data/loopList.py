# You can loop through the list items by using a for loop

testList = ["python", "java", "c++", "c#", "javascript", "typescript"]

for x in testList:
    print(x)
# Compare this snippet from 4.List%20type%20data/loopList.py:
# # Loop through the list items
#

testList2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for x in testList2:
    if(x%2 == 0):
        print(x)


# while loop

y = 0

while y < len(testList2):
    if(testList2[y] % 2 == 0):
        print(f"testList2[{y}] = {testList2[y]}")
    y += 1
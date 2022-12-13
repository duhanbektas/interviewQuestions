
#This one is for the example that is given on the question
example = [3, None, 2, None, None, 1, False, None, 10]

for i in range(len(example)):
   if example[i] is None:
     example[i] = example[i-1]
print(example)


#If 'USER' provides the elements and we need to do it for empty strings;
myList = []
  
# number of elements as input
n = int(input("Enter number of elements : "))
  
# iterating till the range
for i in range(0, n):
    element = input('Enter elements:')
    myList.append(element)

#if element is empty, previous element will be replace it:
for j in range(0,len(myList)):
    if myList[j] == '':
      myList[j] = myList[j-1]

print(myList)
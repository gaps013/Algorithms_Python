import random
def binary_search(input_array,start,end,number):
  middle = start+(end-start)//2
  if(end>=start):
    if(number == input_array[middle]):
      return middle
    elif(number>input_array[middle]):
      return binary_search(input_array,middle+1,end,number)
    elif(number<input_array[middle]):
      return binary_search(input_array,start,middle-1,number)
  else:
    return -1
input_array = random.sample(range(1, 10000), 100)
input_array.sort()
key= 9981
index_position = binary_search(input_array,0,len(input_array)-1,key)
if(index_position!=-1):
  print("Element found at index position ",index_position)
else:
  print("Element not found")

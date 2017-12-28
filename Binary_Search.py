import random
def binary_search(input_list,start,end,number):
  middle = start+(end-start)//2
  if(end>=start):
    if(number == input_list[middle]):
      return input_list[middle]
    elif(number>input_list[middle]):
      return binary_search(input_list,middle+1,end,number)
    elif(number<input_list[middle]):
      return binary_search(input_list,start,middle-1,number)
  else:
    return -1
input_list = random.sample(range(1, 10000), 100)
input_list.sort()
print(binary_search(input_list,0,99,input_list[91]))
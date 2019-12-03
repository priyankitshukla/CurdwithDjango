numbers=[5,1,76,22,10]
numbers.append(78)
print(numbers)
print(len(numbers))
## insert to begining

numbers.insert(0,100)
print(numbers)
numbers.sort()
print(numbers)
numbers.sort()
numbers.reverse()
print(numbers)
numbers2=numbers.copy()
print(numbers)

# WAP to remove duplicate employee from lis

list = [1,2,3,4,5,23,5,432,6,23]
unique_list=[]
for item in list:
    if item not in unique_list:
        unique_list.append(item)
print(unique_list)
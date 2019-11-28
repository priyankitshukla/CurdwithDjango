i = 1
while i <= 5:
    print('value of i is ' + str(i))
    i = i+1

j=1
while j<=5:
    print('*' * j)
    j=j+1

#
# # Secret game
#
# magic_number=9
# max_try=3
# current_try=0

# while current_try<max_try:
#     guess=int(input('Guess a number between 1-9: '))
#     current_try=current_try+1
#     if guess==magic_number:
#         print('You Win')
#         break
#     if current_try==max_try:
#         print('You lost')

# while current_try<max_try:
#     guess=int(input('Guess a number between 1-9: '))
#     current_try=current_try+1
#     if guess==magic_number:
#         print('You Win')
#         break
# else:
#     print('You lost')


#####################################For loop #######################################

# for item in 'Python':
#     print(item)

# for item in ['Priyankit', 'HCL', 'Technology']:
#     print(item)

# for item in [1,2,3,4,5,6]:
#     print(item)


############## Range in python

# for item in range(10):
#     print(item)

# for item in range(5, 10):
#     print(item)
# total=0
# prices=[10, 20, 30]
# for price in prices:
#     total+=price
# print(f' Total price- {total}')


### Generate coordinates

# for i in range(4):
#     for j in range(3):
#         print(f'{i,j}')


# numbers=[5,2,5,2,2]
# for number in  numbers:
#     print('*' * number)


# Write a program to find largest number in list

numbers = range(100)
max_number = numbers[0]
for number in numbers:
    if number > max_number:
        max_number = number
print(max_number)
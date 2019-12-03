# enter a alpha numeric value intead of integer value to exception comes.
# age=int(input('Age : '))
# print(age)

try:
    age = int(input('Age : '))
    print(f'Age ={age}')
    risk = 2000 / age
    print(f'Risk = {risk}')
except ValueError:
    print('Please try again.')
except ZeroDivisionError:
    print(f'Age cant be {age}')
# Exception handling

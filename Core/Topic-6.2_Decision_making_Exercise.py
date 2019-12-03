# Practice test
# take input from user for name and current working country if india print offshore or Onsite.


name = input('Enter your name : ')

country = input('Enter your country name : ')

if country.lower() == 'india':
    print(f'{name} belongs to Offshore')
else:
    print(f'{name} Employee belongs to Onsite')



# Decision making    if elif

is_Hot = False
is_Cold = False

if is_Hot:
    print('''
        Its very hot day

        Drink Plenty of water
        ''')
elif is_Cold:
    print('Its a cold day')
else:
    print('Its a lovely day')
print('Enjoy your day!')

# Excersise with logical operator
if is_Cold == False and is_Hot == False:
    print("Both condidtion's are false")

if is_Cold == False and not is_Hot:
    print("Both condidtion's are false")

# condition
temperature = 30

if temperature > 30:
    print('Hot Day')
elif temperature < 30 and temperature > 20:
    print('Lovely day')
else:
    print('Cold day')
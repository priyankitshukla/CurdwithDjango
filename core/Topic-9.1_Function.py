# convention use def to define a function, name should be in lower case if multiple words seperate with a underscore.

def greet_hcl():
    print("Hello HCL")

def sum(a,b):
    return  a+b
print("Start of function")
greet_hcl()
print("End of Function")
print(sum(5,5))


## keyword argument to swap the position

def greet_hcl(first_name,last_name):
    print(first_name+' '+last_name)

greet_hcl('HCL','Technology')
# change the sequence
greet_hcl('Technology','HCL')

greet_hcl(last_name='Technology',first_name='HCL')
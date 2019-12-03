# All parameters (arguments) in the Python language are passed by reference. It means if you change what a parameter
# refers to within a function, the change also reflects back in the calling function. For example −

# Function definition is here

def changeme( mylist ):
   #"This changes a passed list into this function"
   mylist = [1,2,3,4]; # This would assig new reference in mylist
   print("Values inside the function: ", mylist)
   return

# Now you can call changeme function
mylist = [10,20,30];
changeme( mylist );
print("Values outside the function: ", mylist)


# Function definition is here
def changeme(mylist):
   # This changes a passed list into this function
   mylist.append([1,2,3,4]);
   print("Values inside the function: ", mylist)


# Now you can call changeme function
mylist = [10,20,30];
changeme( mylist );
print ("Values outside the function: ", mylist)
name = {
    "name": "Priyankit",
    "organization": "HCL Technology",
    "age": 40
}


for resource in name:
    print(resource)
#
#
records = [
     {
         "name" : "Priyankit",
         "organization" : "30",
         "age" : 40
     },
     {
         "name" : "HCL",
         "organization" : "HCL",
         "age" : 42
     }
     ]

for record in records:
     print(record)
     print(record.get('name'))


######### Create a dictionary of Employee name age org ##############


digits = input("Enter Number")
digits_map = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four"
}

for num in digits:
    print(digits_map.get(num))

# for more visit https://www.datacamp.com/community/tutorials/json-data-python

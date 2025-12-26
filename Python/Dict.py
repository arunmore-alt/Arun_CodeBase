print("Dictnary in Python...!!!")

my_dict = {'name': 'Arun', 'age': 30, 'city': 'Chennai'}
print(my_dict)
print(type(my_dict))
print(my_dict['name'])
print(my_dict.get('Animal'))
my_dict['age'] = 31
print(my_dict)
my_dict['profession'] = 'Engineer'
print(my_dict)
print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())
print(len(my_dict))
for key in my_dict:
    print(f"{key} : {my_dict[key]}")

if 'city' in my_dict:
    print("City is present in the dictionary")
else:
    print("City is not present in the dictionary")

my_dict.pop('profession')
print(my_dict)
del my_dict['age']
print(my_dict)
print(len(my_dict))

my_dict2 = {'country': 'India', 'language': 'Python'}
my_dict.update(my_dict2)
print(my_dict)

emp ={}
print(emp)



# Excersice 


for i in range(7):
    print(i)
else:
    print("Loop is completed")


# in this case Loop does not complete (end) beacuse loop is break

for i in range(5):
    print(i)
    if i==3:
        break
else:
    print("Loop is completed")

print("Enumerate Function in Python...!!!")

marks = [56,78,990,45,34,89]

index = 0
for mark in marks:
    print(mark)
    if index == 3:
        print("Index is 3")
    index +=1


# index -> value 
print("Using Enumerate Function...")
for index, mark in enumerate(marks):
    print(mark, " ", index)
    if index ==3:
        print("Index is 3")


print("Using Enumerate Function...")
for index, mark in enumerate(marks, start=1):
    print(mark, " ", index)
    if index ==3:
        print("Index is 3")


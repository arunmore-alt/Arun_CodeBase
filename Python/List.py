print("List.....!!!!!")

# fruits = ["Apple", "Banana", "Mango", "Grapes"]
# print(fruits)
# print(type(fruits))

# print(fruits[0])
# print(fruits[1])

# print(fruits[-1])

# print(fruits[1:3])
# print(fruits[::2])
# print(fruits[::-1])

# # Modifying List
# fruits[1] = "Orange"
# print(fruits)
# print(len(fruits))
# print(id(fruits))
# print(fruits.append("Pineapple"))
# print(fruits)
# print(fruits.insert(1,"Kiwi"))
# print(fruits)
# print(fruits.remove("Mango"))
# print(fruits)
# print(fruits.pop())
# print(fruits)
# print(fruits.pop(1))
# print(fruits)
# print(fruits.sort())
# print(fruits)
# print(fruits.reverse())
# print(fruits)
# print(fruits.count("Apple"))
# print(fruits.extend(["Watermelon","Papaya"]))
# print(fruits)
# print(fruits.index("Grapes"))
# print(fruits.clear())
# print(fruits)

# l = [i*i for i in range(1,11) if i%2==0]
# print(l)
# print("Done...!!!")

# P = [j for j in fruits if "a" in j.lower()]
# print(P)

# if P == []:
#     print("List is empty")


L = [3,4,5,5,7,6,8,7,97,3,42,4,245,3,6]
# print(L)
# for i in L:
#     print(i)
# print("-----")
# L.sort()
L.sort(reverse=True)
print(L)


# don't Use this 
m = L
m[1] = 45
print(m)
print(L)
print(id(L))
print(id(m))


# Both L and m Are Different Objects
m =L.copy()
m[2] = 78
print(m)
print(L)
print(id(L))    
print(id(m))




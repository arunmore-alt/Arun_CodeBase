print("Set...!!!")

s1 = {2,3,4,5,6,"djkf"}
print(s1)


s = {1,2,3,4,5,6,7,8,9}
print(s)
print(type(s))
print(len(s))
s.add(10)
print(s)
s.add(5)
print(s)
s.remove(3)
print(s)

# Empty Dictionary
s3={}
print(type(s3))

# empty Set
s4=set()
print(type(s4))
s4.add(100)
s4.add(200)
print(s4)
print(len(s4))
# print(s4[0]) # TypeError: 'set' object is not subscriptable
print("Done...!!!")

for i in s:
    print(i)

a = {1,2,3,4,5}
b = {4,5,6,7,8}
# print(a.union(b))
# print(a.intersection(b))
# a.update(b)
# print(a)
# print(a,b)

# a.intersection_update(b)
# print(a,b)
# a.difference_update(b)
# print(a,b)

c = a.symmetric_difference(b)
print(c)

c.add(1000)
print(c)

# remove vs discard
c.remove(1000)
print(c)

# c.remove(2000) # KeyError: 2000
c.discard(2000)
print(c)


item = c.pop()
print(c)
print(item)
del  c 
# print(c)# NameError: name 'c' is not defined


s1.clear()

information = {"banana", "apple", "mango", "orange"}

if "banana" in information:
    print("Yes, Banana is presenrt in the set And Deleting it now")
else:
    print("No, Banana is not present in the set")


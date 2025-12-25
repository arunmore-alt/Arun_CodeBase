print("Tupples")


tup = ( 1,2,3,45,5,6,7,8,9)
print(tup)
print(type(tup))
print(tup[0])
# tup[3] = 100
print(tup)
print(tup.count(5))
print(tup.index(45))
tup2 = (100,200,300)
tup3 = tup + tup2
print(tup3)
print(len(tup3))
for i in tup3:
    print(i)
print("Done...!!!")
tup4 = (1,2,3, (4,5,6), [7,8,9])
print(tup4)
print(tup4[3])
print(tup4[4])
tup4[4][0] = 70
print(tup4)
print("Done...!!!")
# tup4[3][0] = 40
# print(tup4)

t = ()
print(t)

t1 = (1,)
print(t1)
print(type(t1))

t5 = tuple(range(1,11))
print(t5)
print(type(t5))
print(t5[::-1])
print("Done...!!!")
# t5[0] = 100
# print(t5)
# t5.append(200)
# print(t5)
t6 = tuple(i*i for i in range(1,11) if i%2==0)
print(t6)
print("Done...!!!")
# t6.sort()
# print(t6) # AttributeError: 'tuple' object has no attribute 'sort'

t7 = tuple(sorted(t6))
print(t7)

print("Done...!!!")
# t7.reverse()
# print(t7) # AttributeError: 'tuple' object has no attribute 'reverse'
t8 = tuple(reversed(t7))
print(t8)
print("Done...!!!")
# t8.sort()
# print(t8) # AttributeError: 'tuple' object has no attribute 'sort'
t9 = tuple(sorted(t8, reverse=True))
print(t9)
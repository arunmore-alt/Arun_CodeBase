print("File input/Output...!!!")

# f = open('Dict.txt') # in this r mode is Default
# f = open('Dict.txt','r')
# # print(f)
# text = f.read()
# print(text)
# f.close()

# f = open('Dict1.txt','w')
# text = f.read()
# print(text)
# f.close()

# f = open('Dict1.txt','a')
# f.write("Hello Sagar..!!")
# f.close()

# f = open('Dict1.txt','w')
# f.write("Hello Sagar..!!")
# f.close()


# with open('Dict.txt','a') as f:
#     f.write("Hi My B-Day is Today")


# Methods in Py

f = open('Dict.txt','r')
# while True:
#     line = f.readline()
#     if not line:
#         break
#     print(line)

# seek and tell function


print(type(f))
f.seek(7)
# data =f.read(4)
data = f.read(6)
print(data)
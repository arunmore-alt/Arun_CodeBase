print("Loops")



for i in range(10):
    print(i)

for j in range(1,11):
    print(j)

for k in range(1,11,2):
    print(k)

for l in range(10,0,-1):
    print(l)

for m in range(10,0,-2):
    print(m)


colours = ["red","green","blue","yellow","purple"]
for colour in colours:
    print(f"The colour is {colour}")
    for i in colour:
        print(i)

print("-----")

# for n in "Python":
#     print(n)


# i = 1
# while i <= 10:
#     print(i)
#     i += 1


# count = int(input("Enter a Number "))
# if count<23:
#     while count<12:
#         print(count)
#         count +=1
# else:
#     print(f"{count} is greater than 23")


# print("Done..!!!")


# brak and continue

# for i in range(1,11):
#     if i ==5:
#         break
#     print(i)
# print("Loop ended")


for i in range(1,11):
    if i ==5:
        continue
    print(i)
print("Loop Ended")


# do while loop simulation

# i = 1
# while True:
#     print(i)
#     i +=1
#     if i >5:
#         break
# print("Loop Ended")



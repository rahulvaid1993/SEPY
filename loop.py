# greeting = "Hi"
#
# if greeting == "Morning":
#     print('true')
# else:
#     print('false')
#
# print('out of if else')
#
# obj = [1, 2, 3, 4, 5, 6]
#
# for i in obj:
#     print(i)
#     print(i * 2)
#
# # sum of first 5 natural numbers
# sum1 = 0
# for j in range(1, 6):
#     print(j)
#     sum1 += j
# print(sum1)
#
# for i in range(1, 10, 2):
#     print("{}{}".format("the values: ", i))
#
# itr = 5
# while itr >= 1:
#     print(itr)
#     itr = itr - 1

for i in range(10, 0):
    if i == 9:
        i += 1
        continue
    if i == 3:
        break
    i += 1
    print(i)

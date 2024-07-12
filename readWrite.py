file = open('test.txt')
# print(file.read())
# print(file.read(2))

# print(file.readline())
# print(file.readline())

# line = file.readline()
#
# while line != "":
#     print(line)
#     line = file.readline()

var = file.readlines()
print(var)


for i in var:
    print(i)




file.close()

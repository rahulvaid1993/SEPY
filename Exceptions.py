ItemsInCart = 0

# if ItemsInCart != 2:
#     raise Exception("rod count not match!!!!")

# assert (ItemsInCart == 0)


# custom way to give exception message

try:
    with open('rv.txt', 'r') as reader:
        print(reader.readlines())
except:
    print('file not opening')

# Python caught exeception instead of custom exception
try:
    with open('rv.txt', 'r') as reader1:
        reader1.readlines()
except Exception as e:
    print(e)
finally:
    print('teardown')

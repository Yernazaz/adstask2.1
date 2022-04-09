from typing import List


# 1ex


def fiveintarray():
    five = [1, 2, 3, 4, 5]
    for x in range(len(five)):
        print(five[x])


# 2ex

def appendtoend():
    five = [1, 2, 3, 4, 5]
    for x in range(len(five)):
        print(five[x])
    print("__________")
    five.append(6)
    for x in range(len(five)):
        print(five[x])


# 3ex


def reversearray():
    five = [1, 2, 3, 4, 5]
    for x in range(len(five) - 1, -1, -1):
        print(five[x])


# 5ex

def appendfromanother():
    five = [1, 2, 3, 4, 5]
    ten = [10, 11, 12, 13, 14]
    print(five)
    print("__________")
    print(ten)
    print("__________")
    for x in range(len(five)):
        five.append(ten[x])
    print(five)


# 6ex


def removespec(n):
    ten = [1, 1, 1, 4, 5, 10, 11, 12, 13, 14]
    for x in range(len(ten)):
        print(ten[x])

    ten.pop(n)

    print("__________")
    for x in range(len(ten)):
        print(ten[x])


# 4ex

def countinarray(n):
    ten = [1, 1, 3, 1, 5, 10, 11, 12, 13, 14]
    for x in range(len(ten)):
        print(ten[x])
    print("__________")
    print(ten.count(n))


# 7ex


def removefirst_(n):
    ten = [1, 1, 3, 1, 5, 10, 11, 12, 13, 14]
    for x in range(len(ten)):
        print(ten[x])
    print("__________")
    ten.remove(n)
    print(ten)


# 8ex


def dub():
    ten = [0, 2, 3, 1, 5, 3, 11, 12, 11, 14, 11, 2, 1]
    dublicate = 0
    print(ten)
    print("-----------")
    index = 1
    for x in range(len(ten)):
        ten1 = ten.copy()
        if ten1.count(ten1[x]) == 2:
            numb = ten1[x]
            index = ten1.index(numb)
            ten1.remove(ten1[x])
            index2 = ten1.index(numb)+1
            print(numb, " First index: ", index, " Second index: ", index2)
            break







if __name__ == '__main__':
    appendfromanother()

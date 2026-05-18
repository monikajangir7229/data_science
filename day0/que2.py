
def add(a, b):
    return a + b



def check(lst, total):

    mid = len(lst) // 2
    middle = lst[mid]

    if total > middle:

        s = set(lst[:mid])
        print("Set:", s)

    elif total == middle:

        d = {mid: middle}
        print("Dictionary:", d)

    else:

        t = tuple(lst[mid+1:])
        print("Tuple:", t)



a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

lst = list(map(int, input("Enter list elements: ").split()))


total = add(a, b)

print("Sum:", total)


check(lst, total)
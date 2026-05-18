import statistics

def matrix(lst):

    while len(lst) < 9:
        lst.append(None)

    for i in range(0, 9, 3):
        print(lst[i:i+3])


def details(lst):

    t = tuple(lst)

    print("Tuple:", t)
    print("Mean:", statistics.mean(lst))
    print("Median:", statistics.median(lst))
    print("Mode:", statistics.mode(lst))


def main(lst):

    print("Matrix:")
    matrix(lst)

    print("\nDetails:")
    details(lst)

lst = list(map(int, input("Enter elements: ").split()))

main(lst)
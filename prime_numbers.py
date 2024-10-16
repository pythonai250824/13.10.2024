
# divided by himself and 1
# 4 / 2 == 2
# 7 / 7 == 1 Rishoni
# 1 not Rishoni
# 2 is Rishoni

#x: int = int(input('give me a number'))

for x in range(1, 100 + 1):
    if x < 1:
        print('must be equal or larger than 1')
    else:
        if x == 1:
            print(f"{x} is not prime")
        else:
            divider: int = 2 # 7
            # improvements:
            # can run only till sqrt
            # can start with 3 and jump by 2
            while divider < x:
                if x % divider == 0:
                    break
                divider += 1
            if divider < x:
                # 1 found a divider
                print(f"{x} is not prime")
            else:
                # 2 divider == x
                print(f"{x} is prime")

list_prime: list[int] = []
for x in range(1, 100 + 1):
    if x < 1:
        continue
    else:
        if x == 1:
            continue
        elif x == 2:
            list_prime.append(x)
        elif x % 2 == 0:
            continue
        else:
            divider: int = 3
            found_divider: bool = False
            while divider <= x ** 0.5 + 1:
                if x % divider == 0:
                    found_divider = True
                    break
                divider += 2
            if not found_divider:
                list_prime.append(x)
print(list_prime)

list_rishoni: list[int] = []
list_rishoni_comp: list[int] = []

for x in range(2, 100 + 1):

    list_divs: list[int] = []
    #   9  9  9  9
    #   2  3  4  5
    # [ 1, 0, 1, 4, 3, 2, 1]
    #   7
    #   2  3  4  5  6
    # [ 1, 1, 3, 2, 1]

    for i in range(2, x):
        list_divs.append(x % i)
    if all(list_divs): # if true the number is prime
        list_rishoni.append(x)
    if all([x % i for i in range(2, x)]):
        list_rishoni_comp.append(x)

print(list_rishoni)
print(list_rishoni_comp)

#  [append(x)   for x in 2.. 100              check if rishoni]
print([x       for x in range(2, 100 + 1)     if all([x % i for i in range(2, x)])])

# without str
# input a number and print how many digits the number has








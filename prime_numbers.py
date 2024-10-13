
# divided by himself and 1
# 4 / 2 == 2
# 7 / 7 == 1 Rishoni
# 1 not Rishoni
# 2 is Rishoni

x: int = int(input('give me a number'))

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



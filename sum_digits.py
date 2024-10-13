
num: int = int(input('enter a number: '))

save: int = num

sum_digit: int = 0

print(num, ': ', end="")
while num > 0:
    ahadot: int = num % 10
    sum_digit += ahadot
    # short: num //= 10
    num = num // 10
    print (f"{ahadot} {"+ " if num > 0 else "= "}", end="")
print(sum_digit)



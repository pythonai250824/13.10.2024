

num: int = int(input('enter a number: '))

digits_count: int = 0
if num == 0:
    digits_count = 1
else:
    while num > 0:
        digits_count += 1
        num = num // 10

print(digits_count)
x = int(input('enter x:'))

if x % 2 == 0:
    print(f"{x} is even")
else:
    print(f"{x} is odd")

desc: str = None
if x % 2 == 0:
    desc = "Even"
else:
    desc = "Odd"

#            true      <if>      else  false
desc: str = "Even" if x % 2 == 0 else "Odd"
print(f"one line: {x} is {"Even" if x % 2 == 0 else "Odd"}")

# Ternary
# tagril 1: input a height between 0.1-2.8
#             print you are tall (if height > 1.8)
#             print you are not tall (if height <= 1.8)
# targil 2: input a number between 0-99
#             print-- the number is 1 digit
#             print-- the number is 2 digit
height: float = None
while True:
    try:
        height = float(input('enter height [0.1-2.8]? '))
        if 0.1 <= height <= 2.8:
            break
    except:
        pass

if height > 1.8:
    print('you are tall')
else:
    print('you are not tall')

word_not: str = ''
if height > 1.8:
    word_not = ''
else:
    word_not = 'not'
print(f"you are {word_not} tall")

print(f"you are {'' if height > 1.8 else 'not'} tall")

number: int = None
while True:
    try:
        number = int(input('enter a number [0-99]? '))
        if 0 <= number <= 99:
            break
    except:
        pass

if number < 10:
    print(f'number {number} is 1 digit')
else:
    print(f'number {number} is 2 digit')

one_or_two: str = ''
if number < 10:
    one_or_two = '1'
else:
    one_or_two = '2'
print(f'number {number} is {one_or_two} digit')

print(f'number {number} is {'1' if number < 10 else '2'} digit')

salary: int = 30_000  # input

percent: float = None
if salary >= 30_000:
    percent = 20
else:
    percent = 10

percent = 20 if salary >= 30_000 else 10
print(f'tax is {salary * percent / 100}')

x: int = int(input('enter number'))
if x > 0:
    print(f"{x} is positive")
elif x < 0:
    print(f"{x} is negative")
else:
    print(f"{x} is Zero")

if x > 0:
    print(f"{x} is positive")
else:
    if x < 0:
        print(f"{x} is negative")
    else:
        print(f"{x} is Zero")

print(f"{x} is {"positive" if x > 0 else ("negative" if x < 0 else "Zero")}")

#                  ["neg", "pos", "pos", "neg", "zero", "pos", "neg"]
list1: int[list] = [   -4,     1,   200,    -3,      0,     2,    -3]
list_res : list[str] = []
for num in list1:
    if num > 0:
        list_res.append("positive")
    else:
        if num < 0:
            list_res.append("negative")
        else:
            list_res.append("zero")

list_res = ["positive" if num > 0 else ("negative" if num < 0 else "Zero") for num in list1]




















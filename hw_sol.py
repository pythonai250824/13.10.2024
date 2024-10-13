import random

bool_list: list[bool] = [random.choice([True, False]) for _ in range(3)]

print('all true?', all(bool_list))

print('any true?', any(bool_list))

print('all false', not all(bool_list))

print('one false at least', not any(bool_list))

five_random: list[int] = [random.randint(-2, 2) for _ in range(5)]
print('5 randoms', five_random)

# five_random: list[int] = []
# for _ in range(5):
#     new_element: int = random.randint(-2, 2)
#     five_random.append(new_element)

print('all not zero', all(five_random))

print('any not zero', any(five_random))

print('all zeros', not any(five_random))

print('at least one zero', not all(five_random))

details: str = "danny from tel aviv"

print('len', len(details))

print('upper', details.upper())

print('upper', details.lower())

print('starts with danny', details.startswith('danny'))

print('ends  with tel aviv', details.endswith('tel aviv'))

splitted: list[str] = details.split()

stars_danny = details.replace(' ', '*')
print(details.replace(' ', '*'))
print(stars_danny)

print('abc1'.isalpha())
print('abc'.isdigit())

ninja_str: list[str] = ['N', 'I', 'N', 'J', 'A']

print(''.join(ninja_str))
print(' * '.join(ninja_str))

print("'e'.upper() in 'hElLo'.upeer()", 'e'.upper() in 'hElLo'.upper())

word: str = "P3ython12"
fixed_str: list[str] = [char.upper() for char in word if not char.isdigit()]
print(fixed_str)
word_again = ''.join(fixed_str)
print(word_again)












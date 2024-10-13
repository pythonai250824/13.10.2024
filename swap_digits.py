
# get 2 digit number
# 97 ==> 79
# 55 ==> 55
# 12 ==> 21
# 90 ==> 09

# 1. str
num_str = "97"
print (f"{num_str[::-1]}")

num_int: int = int(num_str)
ahadot: int = num_int % 10
asarot: int = num_int // 10
# 2. int, mathematics
# 97 = 90 + 7 = 9 * 10 + 7 * 1 ==> 7 * 10 + 9 * 1 = 79
# asarot 9
# ahadot 7
# 7 * 10 + 9 * 1 = 79
new_number: int = ahadot * 10 + asarot * 1

# ** Bonus: switch digits or any length number
# 3784 = 3 * 1000 + 7 * 100 + 8 * 10 + 4 * 1
# 4 * 10 + 8 = 48
# 48 * 10 = 480 + 7 = 487
# 487 * 10 = 4870 + 3 = 4873



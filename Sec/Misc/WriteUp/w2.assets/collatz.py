import string

CURR_ASCII = string.printable

num = 109
contain = chr(num)
while num != 1:
    if num % 2 == 1:
        num = num * 3 + 1
    else:
        num = num // 2
    if chr(num).isascii() and chr(num) in CURR_ASCII:
        contain += chr(num)

print(contain)

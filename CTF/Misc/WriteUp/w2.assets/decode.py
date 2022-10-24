import random


def gen_random_key(secret_seed):
    random_poor = []
    random.seed(secret_seed)
    for _ in range(10):
        random_poor.append(str(random.random())[2:])
    return random_poor[-1], random_poor[0]


def decode_01(flag_part1, random_key):
    assert (len(flag_part1) == 16 and len(flag_part1) == 16)
    flag_arr = bytearray(flag_part1)
    res = ""
    for i in range(len(flag_arr)):
        res += chr(flag_arr[i] ^ int(random_key[i]))
    return res


def decode_02(str1, str2):
    res = ""
    for index, value in enumerate(str1):
        res += chr(value - int(str2[index]))
    return res


if __name__ == '__main__':
    # the result is: alin|]^edk7neYCkR2xrbHap3r~#@,&~
    crypt_flag = b"alin|]^edk7neYCkR2xrbHap3r~#@,&~"
    key = gen_random_key('mR)|>^/Gky[gz=\.F#j5P(')
    decode01 = decode_01(crypt_flag[0:16], key[0])
    decode02 = decode_02(crypt_flag[16:], key[1])
    print(decode01 + decode02)

from os import urandom


def crack_key():
    res = ()
    temp_list = []
    for _ in range(1000000):
        temp_list.append(urandom(1))
    res = set(temp_list)
    return res


def fuck_xor(cyber, key):
    res = []
    print(key)
    for i in range(len(cyber)):
        res.append(cyber[i] ^ key[0])
    return bytes(res)


if __name__ == '__main__':
    key_container = crack_key()

    with open("./output.txt", "rb") as reader:
        fd = reader.read()
    fd = str(fd)[2:-1]

    cyber = [int(fd[i] + fd[i + 1], 16) for i in range(0, len(fd), 2)]
    #  print(cyber)
    for i in key_container:
        res = fuck_xor(cyber, i)
        print(bytearray(res))

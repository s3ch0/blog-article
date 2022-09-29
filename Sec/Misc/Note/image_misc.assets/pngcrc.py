# coding=utf-8
# author : secho
# email  : zhouhaobusy@gmail.com
# blog   : www.zhouhaobusy.com

import sys
import zlib
import os
import struct
import codecs

DEFAULT_TEMP_FILE_NAME = "output.png"


def gain_utils(file_name):
    with open(file_name, "rb") as reader:
        data = bytearray(reader.read())
    IHDR_ChunkData = data[12:29]
    new_crc = hex(zlib.crc32(IHDR_ChunkData))
    crc32key = codecs.encode(data[29:33], "hex").decode("ascii")
    crack_info = (IHDR_ChunkData, "0x" + crc32key)
    return crack_info, new_crc


def crack(IHDR_ChunkData, crc32key):
    try_data = IHDR_ChunkData
    max_num = 0xfff #理论上0xffffffff,但考虑到屏幕实际，0x0fff就差不多了
    for width in range(max_num): # 高和宽一起爆破
        width_data = bytearray(struct.pack('>i', width)) #q为8字节，i为4字节，h为2字节
        for height in range(max_num):
            height_data = bytearray(struct.pack('>i', height))
            try_data[4:8] = width_data
            try_data[8:12] = height_data
            crc32result = zlib.crc32(try_data)
            if crc32result == int(crc32key, 16):
                c_width = codecs.encode(width_data, "hex").decode("ascii")
                c_height = codecs.encode(height_data, "hex").decode("ascii")
                print("\33[34m" + "[+] Currect Width: {} Height: {}".format(
                    c_width, c_height) + "\33[0m")
                return width_data, height_data


def fix_file(file_name, cwidth, cheight):
    with open(file_name, "rb") as reader:
        data = bytearray(reader.read())
    data[16:20] = cwidth
    data[20:24] = cheight
    if os.path.exists(DEFAULT_TEMP_FILE_NAME):
        print("\33[33m" +
              "[!] This path exists {}".format(DEFAULT_TEMP_FILE_NAME) +
              "\33[0m")
        exit(1)
    with open(DEFAULT_TEMP_FILE_NAME, "wb") as writer:
        writer.write(data)


def change_path():
    global DEFAULT_TEMP_FILE_NAME
    export_filename = sys.argv[2]
    DEFAULT_TEMP_FILE_NAME = export_filename
    return None


if __name__ == '__main__':
    argc = len(sys.argv)
    assert (argc <= 3)
    file = sys.argv[1]
    if (argc == 3):
        change_path()
    crack_info, new_crc = gain_utils(file)
    meta_info = crack(*crack_info)
    if meta_info == None:
        print("\33[31m" + "Crack Width and Height failed!" + "\33[0m")
        exit(1)
    fix_file(file, *meta_info)
    print("\33[32m" +
          "[*] The correct image ({}) was successfully exported".format(
              DEFAULT_TEMP_FILE_NAME) + "\33[0m")

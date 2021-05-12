#!/usr/bin/env python3

# reframe.git/reframe/utility/systeminfo.py
# import contextlib
# import glob
import os
import re
# import reframe.utility.osext as osext
# from reframe.core.exceptions import SpawnedProcessError

def bits_from_string(mask):
    ret = []
    mask_int = int(mask, 0)
    index = 0
    while mask_int:
        if mask_int & 1:
            ret.append(index)

        index += 1
        mask_int >>= 1

    return ret

def string_from_bits(ids):
    ret = 0
    for id in ids:
        ret |= (1 << id)

    return hex(ret).upper()

if __name__ == "__main__":
    # 'arch': 'broadwell'
    # {'numa_nodes': ['0x00003FFFF00003FFFF', '0xFFFFC0000FFFFC0000']
    # systeminfo_jg.bits_from_string('0x00003FFFF00003FFFF')
    # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53]
    hex_in = '0x00003FFFF00003FFFF'
    cpu_list = bits_from_string(hex_in)
    print(f'in={hex_in}\nout={cpu_list}')

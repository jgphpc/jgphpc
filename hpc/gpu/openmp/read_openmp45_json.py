#!/usr/bin/env python3

# --- OpenACC_Validation_Testsuite_SCS ==> openmp tab
# results on google sheets: paste then right click then split into columns
#
# .json file must start with:
# [
#   {
#     "Binary path": "bin/linked_list.c",
# and end with:
#     "Test system": "daint"
#   }
# ]

import argparse
import glob
import sys
import os
import json
from pprint import pprint


def main():
    '''xxx'''
    data = json.load(open('results.json'))
    for ddd in data:
        test_name = ddd['Test name']
        test_path = ddd['Test path'].split('/')[:-1]
        test_path = '/'.join(test_path)
        test_compile_result = ddd['Compiler result']
        test_run_result = ddd['Runtime result']
        print(test_path,",",
            test_name,",",
            test_compile_result,",",
            test_run_result)
    print("ok")


if __name__ == "__main__":
    main()


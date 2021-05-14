#!/usr/bin/env python

# echo -e "sdfa \n sdgf" |./io.py --stdin
# ./io.py ./in

import sys


def myfun(content):
    try:
        ln = 1
        for line in content:  # f.readlines():
            line2 = line.strip()  # remove space at ^ and $
            line = line.rstrip("\n")
            if line2 != "":
                print(f"{ln}. {line}")
                # print("{}. {}".format(ln, line) )
                ln += 1
    except:
        sys.stderr.write("Read error file: {}\n".format(sys.argv[1]))
    # finally:
    #     quit()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        # takes 1 arg:
        sys.stderr.write("Usage: {} <myfile>\n".format(sys.argv[0]))
        sys.exit(1)

    if sys.argv[1] == "--stdin":
        myfun(sys.stdin)
        # pass
    else:
        try:
            f = open(sys.argv[1], "r")
            myfun(f.readlines())
            f.close()
        except:
            sys.stderr.write("Read error2")

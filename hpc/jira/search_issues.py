#!/usr/bin/env python3

import sys
#import re
#import json
from jira import JIRA
# from pprint import pprint


#{{{ --- my functions:
#{{{ connect:
def init_jira():
  jira_url = 'https://jira.cscs.ch'
  passwordjg = read_password_jira()
  jira = JIRA(server=jira_url, basic_auth=('piccinal', passwordjg))
  return jira

def read_password_jira():
    with open('__passwordjg__', 'r') as f:
        passwordjg = [x.strip() for x in f]
    return passwordjg[0]
#}}}

#}}}


# {{{ --- starthere:
if __name__ == "__main__":
    """awk '{print "./search_issues.py "$1}' mytags
./search_issues.py _JGapi
./search_issues.py _JGbenchmark
./search_issues.py _JGc++

    ./search_issues.py _JGdebug
PRIVATE-277 ddt: debug shifter image (outside by attaching to running process)
PRIVATE-481 "Create memory leak reframe check (using scorep)"
PRIVATE-237 ddt: debug shifter image (inside)
PRIVATE-463 "Create valgrind4hpc reframe check"
PRIVATE-472 "test LLVM sanitizer support"
PRIVATE-473 "test ATP support"
    """
    my_jira = init_jira()
    #### myissues.delete()

#{{{ Argument list:
    my_tag = sys.argv[1]
    # print ('Argument list:', str(sys.argv))
    # print(sys.argv[0])
#}}}
    my_search = 'project = "My private tasks" AND status != Done AND description ~ ' + my_tag
    my_issues = my_jira.search_issues(my_search)
    for i in my_issues:
        print("{} {}".format(i.key, i.fields.summary))
#}}}

exit(0)


#!/usr/bin/env python3

import sys
import re
from jira import JIRA
# from pprint import pprint
from itertools import islice


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

#{{{ create_dict_jira:
def create_dict_jira(my_title, my_description):
    my_issue_dict = {
        'project': {'id': 11400}, #  my private
        'summary': my_title,
        'description': my_description,
        'issuetype': {'name': 'Task'},
        'priority': {'name': 'Low'},
    }
    # print("---- my_issue_dict=\n", my_iid)
    return my_issue_dict
#}}}
#}}}

#{{{ --- starthere:
if __name__ == "__main__":
    # https://jira.readthedocs.io/en/master/examples.html#issues

    # --- connect to JIRA:
    my_jira = init_jira()

    # read in and add tag to issue's description:
    f=open('new', 'r')
    #for i in range(4):
    for i in range(42):
        ll=islice(f, 4)
        # [print('x:',l) for l in ll]
        my_list = []
        for l in ll:
            my_list.append(l)
        my_title = my_list[0].strip()
        my_text = my_list[1].strip()
        my_tag = '_JG' + my_list[2]
        my_description = my_tag + my_text
        my_dict = create_dict_jira(my_title, my_description)
        print('my_dict=', my_dict)
        new_issue = my_jira.create_issue(fields=my_dict)
        #print('my_list=', my_title, my_description)
        #print('----')
        print("Created issue:{}\n".format(new_issue))
    f.close()

#}}}

exit(0)

#{{{
# data['issues'][12]['description']
# data['issues'][12]['iid']  # https://git.cscs.ch/piccinal/perfhackaton/issues/30
# data['issues'][12]['id']
# data['issues'][12]['state']
# data['issues'][12]['title']
#print("\n ------------------\nissue_i={} len={} iid={} title={} desc={} notes=\n".format(
#            issue_i, notes_len, my_iid, my_title, my_description))
# print(data['issues'][issue_i])
#}}}


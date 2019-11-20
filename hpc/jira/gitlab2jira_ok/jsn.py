#!/usr/bin/env python3

# export gitlab2jsn then ./jsn.py
#     --- creating issue_i=26 iid=31 title=extrap
#     new_issue={}  PRIVATE-259
#    
#     --- creating issue_i=27 iid=33 title=vtune
#     new_issue={}  PRIVATE-260
#    #uploading: ./uploads/0f3cc56886f7f1291a78c60c89d162d8/Screen_Shot_2018-08-01_at_13.26.31.png

import sys
import re
import json
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

#{{{ create_dict_jira:
def create_dict_jira(mydata, issue_i):
    # N=len(mydata['issues'][12]['notes']);[print(mydata['issues'][12]['notes'][i]['note']) for i in range(N)]
    my_iid = mydata['issues'][issue_i]['iid']
    my_title = mydata['issues'][issue_i]['title']
    # description:
    my_description = ''
    my_description = mydata['issues'][issue_i]['description']
    # notes/comments:
    notes_len = len(mydata['issues'][issue_i]['notes'])
    my_notes = ''
    for j in range(notes_len):
        my_notes += mydata['issues'][issue_i]['notes'][j]['note']
    if my_notes:
        if my_description:
            my_description += my_notes
        else:
            my_description = my_notes
    my_issue_dict = {
        'project': {'id': 11400}, #  my private
        'summary': my_title,
        'description': my_description,
        'issuetype': {'name': 'Task'},
        'priority': {'name': 'Low'},
        # 'gitlabid': my_iid,
    }
    # print("---- my_issue_dict=\n", my_iid)
    return my_issue_dict
#}}}

#{{{ create_attachment:
def create_attachment(mytext):
    uploads_found = str(re.findall(r'/uploads/.*\)', mytext))
    #print('uploads_found')
    #print('uploads_found=', uploads_found, type(uploads_found))
    # >>> [print(SSS[i]) for i in range(len(SSS))]
    if uploads_found:
        myfiles_to_upload = uploads_found.replace('/uploads/', '\n./uploads/').replace(')', '\n)')
        #myfiles_to_upload= []
        #for ii in range(len(uploads_found)):
        #    myfiles_to_upload += uploads_found[ii].replace('/uploads/', '\n./uploads/').replace(')', '\n)')
        result = re.findall(r'^./uploads/.*', myfiles_to_upload, re.MULTILINE)
    else:
        result = []
    return result

#}}}

def upload_attachment_jira(my_attachment, new_issue):
    for i_my_attachment in range(len(my_attachment)):
        print('#uploading: {}'.format(my_attachment[i_my_attachment]))
        upf = my_attachment[i_my_attachment]
        my_jira.add_attachment(issue=new_issue, attachment=upf)

#}}}

#{{{ --- starthere:
if __name__ == "__main__":
    # https://jira.readthedocs.io/en/master/examples.html#issues

    # --- connect to JIRA:
    my_jira = init_jira()

#{{{ Argument list:
    # print ('Argument list:', str(sys.argv))
    # print(sys.argv[0])
    # project_key = sys.argv[1]
#    task_summary = sys.argv[1]
#    task_description = sys.argv[2]
#}}}

    # --- create_dict:
    mydata = json.load(open('project.json'))
    #for issue_i in range(len(mydata['issues'])):
    for issue_i in range(2, len(mydata['issues'])):
    #for issue_i in {160, 161, 162}:
    #for issue_i in {161}:
        my_iid = mydata['issues'][issue_i]['iid']
        my_title = mydata['issues'][issue_i]['title']
        print("\n --- creating issue_i={} iid={} title={}".format(
              issue_i, my_iid, my_title))
        my_issue_dict = create_dict_jira(mydata, issue_i)
        # print("---- my_issue_dict=\n", my_issue_dict)
        #print("---- my_issue_dict={}\n".format(my_issue_dict['description']))

        # --- create_issue: 
        new_issue = my_jira.create_issue(fields=my_issue_dict)
        #new_issue = my_jira.search_issues('project = "My private tasks" AND key = PRIVATE-213')
        print(' new_issue={} ', new_issue) #  new_issue= PRIVATE-213

        # --- uploads_attachment(s):
        # https://jira.readthedocs.io/en/master/examples.html#attachments
        my_attachment = create_attachment(my_issue_dict['description'])
        #print(my_attachment, type(my_attachment))
        if my_attachment:
            upload_attachment_jira(my_attachment, new_issue)
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


#!/bin/bash

source ~/myvenv_dom/bin/activate
jirashell -s 'https://jira.cscs.ch' -u 'piccinal' -p ''

issue = jira.issue('C4KCUST-185') # epic=addon/labels=UserLab/components=CSCSManaged/fix=_epic
issue.fields.summary

# --- issue.fields: 
# project = <JIRA Project: key='C4KCUST', name='C4K Customer Services', id='13400'>
# assignee = <JIRA User: displayName='Jean-Guillaume Piccinali (CSCS)', key='piccinal', name='piccinal'>
# attachment/comment/environment
# components = CrayManaged/CSCSManaged = [<JIRA Component: name='Cray Managed', id='16500'>]
# labels = ['CrayPE', 'Shasta'] / 
# creator/subtasks
# description/summary
# issuelinks
# issuetype = <JIRA IssueType: name='Task', id='10100'>
# priority = <JIRA Priority: name='Medium', id='3'>
# status/reporter/watchers

# https://jira.cscs.ch/rest/api/latest/issue/createmeta
# https://jira.readthedocs.io/en/master/examples.html#issues
issue_dict = {
    'project': {'id': 13400},
    'issuetype': {'name': 'Task'},
    'assignee': {'name': 'piccinal'},
    'components': [{'name': 'CSCS Managed'}],  # only 1!
    'fixVersions': [{'name': 'CSCS-AddOns-PE21.04'}],  # same as epic, only 1!
    'labels': ['UZH', 'UserLab', 'ship-it'],
    'summary': 'scalasca/2.6',
    'description': 'https://www.scalasca.org/scalasca/software/scalasca-2.x/download.html',
    'priority': {'name': 'Low'},
}
new_issue = jira.create_issue(fields=issue_dict)
# new_issue.update(assignee={'name': 'piccinal'}) 

#ok # new_issue is https://jira.cscs.ch/browse/C4KCUST-268
#ok new_issue = jira.issue('C4KCUST-268')   # scalasca/2.6
#ok 
#ok # https://github.com/totallytot/support-scripts-and-configs-for-atlassian-products/blob/master/python/create-task-from-JQL/task.py#L17
#ok existingComponents = []
#ok for component in issue.fields.components:
#ok     existingComponents.append({"name" : component.name})
#ok     # print(existingComponents) # [{'name': 'CSCS Managed'}]
#ok     # issue.fields.components
#ok     #   [<JIRA Component: name='CSCS Managed', id='16501'>]
#ok new_issue.update(fields={'components': [{'name': 'CSCS Managed'}]}) # <--- OK
#ok # issue_dict['components'] = existingComponents
#ok 
#ok existingVersion = []
#ok for version in issue.fields.fixVersions:
#ok     existingVersion.append({"name" : version.name})
#ok     # print(existingVersion) # [{'name': 'CSCS-AddOns-PE21.04'}]
#ok     # issue.fields.fixVersions:
#ok     #   [<JIRA Version: name='CSCS-AddOns-PE21.04', id='23300'>]
#ok new_issue.update(fields={'fixVersions': [{'name': 'CSCS-AddOns-PE21.04'}]}) # <--- OK
#ok # issue_dict['fixVersions'] = existingVersion
#ok 
#ok # issue_dict['summary'] = issue.fields.summary
#ok # issue_dict['customfield_10002'] = issue.fields.customfield_10002
#ok # issue_dict['priority'] = { 'id': issue.fields.priority.id, 'name': issue.fields.priority.name }

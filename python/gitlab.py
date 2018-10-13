#!/opt/python/17.09.1/bin/python3

# https://madra.cscs.ch/scs/doc
# https://docs.gitlab.com/ee/api/issues.html#list-project-issues
# curl --header "PRIVATE-TOKEN: -sSvLb7FsfjjoVyEsncA" https://madra.cscs.ch/api/v4/projects/18/issues/162

# import numpy as n
# print(n.__version__)

import json
from pprint import pprint

data = json.load(open('eff.json'))
# print (json.dumps(data,indent=2,sort_keys=True))
#pprint(data)
#print (data["100"]["id"])

print("|author|assigned|title|url|")
print("|------|--------|-----|---|")
for d in data:
    #print(d["iid"])
    iid=d["iid"]
    auth = d["author"]["username"]
    title = d["title"]
    url = d["web_url"]
    if d["assignee"]:
        #print ('assigned to: {}'.format(d["assignee"]["username"]))
        ass=d["assignee"]["username"]
    else:
        #print ('assigned to: Unassigned')
        ass = 'nobody'

    #ok: print("author:{0:<10} assigned:{1:<10} title:{2:<30s} {3:<41s}".format(auth[0:10], ass[0:10], title[0:30], url))
    print("| {0:<10} |{1:<10} |{2:<30s} |{3:<41s}|".format(auth[0:10], ass[0:10], title[0:30], url))
    #print('author:{:10} assigned:{:10s} title:{:20s} {:41s}'.format(auth, ass, title, url))
    #print('issue:{} author:{} assigned:{} title:{} url:{}'.format(iid,auth,ass,title,url))

# print (data[0]["iid"])
# print ('assigned to: {}'.format(data[0]["assignee"]["username"]))
# print ('created  by: {}'.format(data[0]["author"]["username"]))


#print ('      title: {}'.format(data[1]["title"])
#print ('        url: {}'.format(data[1]["web_url"]))


#for i in data[0]:
#    print(i[0])

# jdata = '{ "name" : "John", "value" : [1,2,3,4,5], "pi" : 3.14 }'
# data = json.loads(jdata)
# print(data)
# print(json.dumps(data))
# print (json.dumps(data,indent=2,sort_keys=True))

# {"name": "John", "value": [1, 2, 3, 4, 5], "pi": 3.14}

# {
#     "name": "John",
#     "pi": 3.14,
#     "value": [
#         1,
#         2,
#         3,
#         4,
#         5
#     ]
# }

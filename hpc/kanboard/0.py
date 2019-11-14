#!/usr/bin/env python3

import kanboard
kb = kanboard.Client('http://localhost/Sites/kanboard/jsonrpc.php', 'admin', 'admin')
x=kb.getmydashboard()

mytime = {}
for i in range(len(x)):
    if x[i]['project_name'] == '2019-2020':
        # mytitle = x[i]['title']
        mykey = x[i]['title'].split(':')[0]
        mytitle = x[i]['title'].split(':')[1]
        if mykey in mytime.keys():
            mytime[mykey] = mytime[mykey] + x[i]['time_spent']
        else:
            mytime[mykey] = x[i]['time_spent']

for i in mytime:
    print(i, mytime[i])

#         myid = x[i]['id']
#         mycolumn = x[i]['column_name']
#         # mytime = x[i]['time_spent']
#         print('{}: {}: {}: {}:'.format(myid, mycolumn, mytime, mytitle))

# x[11]['title'].split(':')[0]
# 'benchm'
# x[11]['title'].split(':')[1]
# ' openacc install gcc'


# for i in sss:
#     print(sss[i])

# ss=s.split(':')

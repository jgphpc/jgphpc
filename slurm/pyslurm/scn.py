#!/usr/bin/env python

# https://wiki.cscs.ch/mediawiki/index.php/Daint%2B_Cray_XC50#Slurm_2
# Taken from pyslurm.git/examples/node_list.py

if __name__ == "__main__":

    import pyslurm
    try:
        hosts = 'nid02048'
        #hosts = "nid03509"        # daint-gpu
        #hosts = "nid000[08-11]"  # daint-mc
        #hosts = "nid00[528-530]"
        #hosts = "nid00[528-530],nid00[580-582]"

        # get first node from the nodelist:
        hlist = pyslurm.hostlist()
        print('hlist=',hlist)
        if hlist.create(hosts):
            #ok print("\tHost list count is {0}".format(hlist.count()))
            #ok print("\tRanged host list is {0}".format(hlist.get().decode('utf-8')))
            #ok print("\tRanged host list is {0}".format(hlist.get_list()[0].decode('utf-8')))
            node = hlist.get_list()[0].decode('utf-8')
            print('node=',node)
            Nodes = pyslurm.node()
            print('Nodes=',Nodes)
            cndict = Nodes.get_node(node)
            print('cndict=',cndict)
            #print(cndict)

            if len(cndict) > 0:
                node_data = cndict[node]
                #print("sockets:", node_data['sockets'])
                #print('node_data', node_data)
                #print("cores:", node_data['cores'])
                #print("cpus:", node_data['cpus'])
                #print("name:", node_data['name'])
                #print("node_addr:", node_data['node_addr'])
                #print("node_hostname:", node_data['node_hostname'])
                #print("tres_fmt_str:", node_data['tres_fmt_str'])
                #keep: print("gres", node_data['gres'][0].split(':')[1])
                if node_data['sockets'] == 2:
                    print("node {0} is broadwell sockets={1}".format(node,node_data['sockets']))
                else:
                    print("node {0} is haswell sockets={1}".format(node,node_data['sockets']))
            else:
                print("No Nodes found !")

# nid00005 :
#    alloc_cpus        : 24
#    cores             : 12
#    cpus              : 24
#    name              : nid00005
#    node_addr         : nid00005
#    node_hostname     : nid00005
#    sockets           : 1
#    tres_fmt_str      : cpu=24,mem=64440M


#OK        node_dict = Nodes.get()
#OK        if len(node_dict) > 0:
#OK            display(node_dict)
#OK            print()
#OK            print("Node IDs - {0}".format(Nodes.ids()))
#OK        else:
#OK            print("No Nodes found !")

    except ValueError as e:
        print("Error - {0}".format(e.args[0]))

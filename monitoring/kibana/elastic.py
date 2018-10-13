#!/usr/bin/env python3

# module load daint-gpu PyExtensions/3.5-CrayGNU-17.08
# pip3 install --user elasticsearch elasticsearch_dsl

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# kibana/visu/arrow/menu: select request instead of table => paste kibana/console
# (https://elasticsearch-dsl.readthedocs.io/en/latest/)
# https://github.com/elastic/elasticsearch-py
# http://elasticsearch-py.readthedocs.io/en/master/index.html
# https://www.elastic.co/guide/en/kibana/master/vis-spy.html
# https://qbox.io/blog/python-scripts-interact-elasticsearch-examples
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


# Get list of slurm jobscripts from kibana for a given gid and month (using range of min/max jobids)
# --- https://github.com/elastic/elasticsearch-dsl-py/issues
# https://www.elastic.co/guide/en/elasticsearch/guide/current/combining-filters.html

from datetime import datetime
from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search
from optparse import OptionParser
# import json

class MyQuery():
    def __init__(self):
        eshost = "sole01.cscs.ch"
        client = Elasticsearch(host=eshost)

# ------------------------
if __name__ == "__main__":

    try:
        # Command line interface
        usage = "usage: %prog -v <version>"
        parser = OptionParser(usage=usage)
        parser.add_option("-v", "--version", action="store", dest="version",
                type="string", help="Data version. Example: 2018030.2823")
        # processing the command line interface
        (options, args) = parser.parse_args()
        if not options.version:
            version = "2018030.2823"
            print('no data-version given, using default:', version)
        else:
            version = options.version
    except Exception as e:
        print(e.args)


    # --- using elasticsearch_py:
    ## query unknown codes from elasticsearch:
    try:
        # client = MyQuery() ==> ("'MyQuery' object has no attribute 'search'",)  ???????
        eshost = "sole01.cscs.ch"
        client = Elasticsearch(host=eshost)

        #  }, { "range": { "timestamp": { "gte": 1519858800000, "lte": 1522533599999, "format": "epoch_millis" } }
        qq = { "size": 0, "query": { "bool": { "must": [ { "query_string": { "query": "data-version:%s" % version, "analyze_wildcard": 'true' }
          }, { "range": { "timestamp": {
              "gte": 1525125600000,
              "lte": 1527803999999,
              "format": "epoch_millis" } }
          } ], "must_not": [] }
          }, "_source": { "excludes": []
          }, "aggs": { "2": { "terms": { "field": "program_known", "size": 10, "order": { "1": "desc" }
          }, "aggs": { "1": { "sum": { "field": "compute_node_hour" } } } } } }
        #top10:  }, "aggs": { "2": { "terms": { "field": "program_known", "size": 10, "order": { "1": "desc" }

# 2018/05: "gte": 1525125600000, "lte": 1527803999999,

        ss = client.search(index="scs*", body=qq)
        #print("Got %d Hits:" % ss['hits']['total'])
    except Exception as e:
        print(e.args)

    try:
        #print(ss['aggregations']['2']['buckets'])
        #print(type(ss['aggregations']['2']['buckets']))
        #print("--- --- ---")
        # --- top unknown codes:
        stopafternunknown = 0
        #dict_exec = {}
        dict_cnh = {}
        for xx in ss['aggregations']['2']['buckets']:
            #while (stopafternunknown < 2):
                stopafternunknown += 1
                dict_cnh[stopafternunknown] = [ xx['key'] ]
                dict_cnh[stopafternunknown].append( round(xx['1']['value'], 2) )
                #print(stopafternunknown,xx['key'],xx['1']['value'])
        #print(dict_exec)
        #print(dict_cnh,type(dict_cnh), type(dict_cnh[1]))
        #print("---")

    except Exception as e:
        print(e.args)


    try:
        # --- get sumofcnh for the percentage:
        ## {1: ['KNOWN', 62662.12], 2: ['sss2', 7064.97], 3: ['exec', 3063.06]}
        totalcnh = 0
        for kk, vv in dict_cnh.items():
            nn = 0
            for vvv in vv:
                nn += 1
                if nn == 2:
                    totalcnh += vvv
                    #print (vvv, totalcnh)
        print('')
        print('| data-version | exec_name | %CNH |')
        print('| ------------ | --------- | ---- |')
        print("|{0:15}|Totalcnh={1:40}|100%|".format(version, round(totalcnh,2)))

        # --- percentage of cnh for each unknown exec:
        # TODO: stopit after 2 ???
        cnh = 0
        for kk, vv in dict_cnh.items():
                nn = 0
                for vvv in vv:
                     nn += 1
                     if nn == 1:
                         exename = vvv
                     if nn == 2:
                         cnh = round(vvv,2)
                         # print(nn,exename,cnh,round(cnh/totalcnh*100,2))
                         print("|{0:15}|{1:40}|{2}%|".format(version, exename, round(cnh/totalcnh*100,1)))
        #print('| ------------ | --------- | ---- |')

#ok        # --- percentage of cnh for each unknown exec:
#ok        cnh = 0
#ok        for kk, vv in dict_cnh.items():
#ok            nn = 0
#ok            for vvv in vv:
#ok                nn += 1
#ok                if nn == 1:
#ok                    exename = vvv
#ok                if nn == 2:
#ok                    cnh = round(vvv,2)
#ok                    # print(nn,exename,cnh,round(cnh/totalcnh*100,2))
#ok                    print("|{0:15}|{1:40}|{2}%|".format(version, exename, round(cnh/totalcnh*100,1)))

    except Exception as e:
        print(e.args)


#example:--- doc_count : 6873 <class 'int'>
#example:--- key : KNOWN <class 'str'>
#example:--- 1 : {'value': 62662.12162699598} <class 'dict'>
#example:
#example:--- doc_count : 11 <class 'int'>
#example:--- key : sss2 <class 'str'>
#example:--- 1 : {'value': 7064.970504760742} <class 'dict'>
#example:
#example:--- doc_count : 1 <class 'int'>
#example:--- key : apes <class 'str'>
#example:--- 1 : {'value': 2976.288818359375} <class 'dict'>


#ok        print(ss['aggregations']['1'])
#ok        print(type(ss['aggregations']['1']))
#ok        print("---")
#ok        print(ss['aggregations']['1']['value'])
#ok        print(type(ss['aggregations']['1']['value']))
        #for cnh in ss['aggregations']['1']:
        #    print(type(cnh))
            #for kk,vv in cnh.items():
            #    print('cnh',kk,vv)


# --- using elasticsearch_dsl:
#_dsl     try:
#_dsl         #client = MyQuery()
#_dsl         eshost = "sole01.cscs.ch"
#_dsl         client = Elasticsearch(host=eshost)
#_dsl #        qq = { "size": 0, "query": { "bool": { "must": [ {
#_dsl #            "query_string": { "query": "data-version:2018030.2823",
#_dsl #            "analyze_wildcard": 'true' } }, { "range": { "timestamp": { "gte":
#_dsl #            1519858800000, "lte": 1522533599999, "format": "epoch_millis" } } } ],
#_dsl #            "must_not": [] } }, "_source": { "excludes": [] }, "aggs": { "2": {
#_dsl #            "terms": { "field": "program_known", "size": 10, "order": { "1": "desc"
#_dsl #            } }, "aggs": { "1": { "sum": { "field": "compute_node_hour" } } } } } }
#_dsl 
#_dsl         ss = Search(using=client, index="scs*") \
#_dsl             .filter("term", category="search") \
#_dsl             .query("match", title="python")
#_dsl         #.exclude("match", description="beta")
#_dsl         #response = ss[0:10000].execute()
#_dsl 
#_dsl         ss.aggs.bucket('per_tag', 'terms', field='tags') \
#_dsl             .metric('max_lines', 'max', field='lines')
#_dsl 
#_dsl         response = ss[0:1].execute()
#_dsl 
#_dsl         for hit in response:
#_dsl             print(hit.meta.score, hit.title)
#_dsl 
#_dsl         for tag in response.aggregations.per_tag.buckets:
#_dsl             print(tag.key, tag.max_lines.value)
#_dsl 
#_dsl     except Exception as e:
#_dsl         print(e.args)



#jg 
#jg client = Elasticsearch(host="sole01.cscs.ch")
#jg 
#jg #q = Q("multi_match", query='match', fields=['_index', 'account'])
#jg #s = Search.query(q)
#jg #s = Search.query("multi_match", query='match', fields=['_index', 'account'])
#jg 
#jg # --- find jobids for this month with:
#jg # > MySQL [stat_csmon]> 
#jg # select job_id from job_accounting where facility='DAINT'
#jg # and job_endtime>'2017-10-31' and job_endtime<='2017-12-01' and group_id='s793'
#jg # order by job_id DESC limit 1;
#jg 
#jg # s702 4167222  4760877
#jg # s793 4258522  4504294
#jg # s753 4257651  4762618 
#jg # s707 4262348  4764219
#jg # pr29 4284922  4765551
#jg # s762 4299869  4769825
#jg # pr11 4250063  4769819
#jg # s624 4262468  4764554
#jg # pr31 4297106  4715033
#jg # ---------------------
#jg # cespos 4762688    4816162
#jg 
#jg     #.query('match', state="COMPLETED") \
#jg     #.query('match', account="pr31") \
#jg # s = Search(using=client, index="slurm*") \
#jg #    .query('match', _index="slurm_01") \
#jg s = Search(using=client, index="scs*") \
#jg     .query('match', cluster="daint") \
#jg     .query('match', partition="normal") \
#jg     .query('match', username="cespos") \
#jg     .filter('range', jobid={'gte': '4762688', \
#jg                              'le': '4816162'})
#jg     #.filter('range', jobid={'gte': '4167222', 'le': '4167224'})
#jg     #.filter('range', jobid={'gte': '4167222', 'le': '4760877'})
#jg 
#jg     #.filter('range', created={'gte': date(2017,11,1), 'lt': date(2017,12,5)})
#jg     #.filter('range',timestamp={'from': '2017-11-01', 'to':'2017-12-01'})
#jg     #.filter('range',timestamp={'gte': '2017-11-01', 'lt': '2017-12-01'})
#jg     #.filter('range',timestamp={'gte': 'now-30d', 'lt': 'now'})
#jg     # s = Search(using=es).filter('term', response=404).filter('range',
#jg     # timestamp={'gte': 'now-5m', 'lt': 'now'})
#jg     #    .query('match', jobid="{* TO 4855281}")
#jg 
#jg # {{{!
#jg #.query('match', jobid="{4855281 TO *}")
#jg # .query('match', account="uzh6") \
#jg #     .query('match', username="cespos") \
#jg 
#jg     #.query('match', @submit="2016-12-14T08:59:08")
#jg     #.query('match', jobid="4818125")
#jg 
#jg #s = Search(using=client, index="slurm*")\
#jg #    .query("match", _index="slurm_01")
#jg 
#jg # .filter("term", category="search") \
#jg #    .exclude("match", description="beta")
#jg 
#jg #s.aggs.bucket('per_tag', 'terms', field='tags') \
#jg #    .metric('max_lines', 'max', field='lines')
#jg # !}}}
#jg 
#jg response = s[0:10000].execute()
#jg print('Total %d hits found.' % response.hits.total)
#jg 
#jg for h in response:
#jg 
#jg     print('jid:{} partition:{} state:{} username:{} account:{}' \
#jg         .format(h.jobid,h.partition,h.state,h.username,h.account) )
#jg     #res={}
#jg     filename = 'eff_' + h.account + '.j' + str(h.jobid)
#jg     fileh = open(filename, "w")
#jg 
#jg     #fileh.write(str(h.jobid)) ;fileh.write("\n")
#jg     #fileh.write(str(h.cpu_hours)) ;fileh.write("\n")
#jg     fileh.write("{}\n{}\n".format(str(h.cpu_hours),str(h.jobid)))
#jg     fileh.write("{}\n".format(h.work_dir))
#jg     fileh.write("state:{}\n".format(h.state))
#jg     try:
#jg         fileh.write("{}\n".format(h.script))
#jg     except:
#jg         fileh.write("no jobscript found\n")
#jg     fileh.close()
#jg 
#jg #     print('jid:{}'.format(h.jobid))
#jg #     print('partition:{}'.format(h.partition))
#jg #     print('state:{}'.format(h.state))
#jg #     #print(h.std_out)
#jg #     print('username:{}'.format(h.username))
#jg #     print('account:{}'.format(h.account))
#jg #     #print('wd:{}'.format( h.work_dir))
#jg #     #print('nodes:{}'.format(h.total_nodes))
#jg #     #print('cpuh:{}'.format(h.cpu_hours))
#jg #     #print('jobscript:{}'.format(h.script))
#jg #     print('')
#jg     #print(h.script)
#jg 
#jg #for tag in response.aggregations.per_tag.buckets:
#jg #    print(tag.key, tag.max_lines.value)

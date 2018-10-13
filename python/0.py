#!/usr/bin/env python

   
quit()


for iii in range(0,6):
    try:
        print(iii,iii/(4-iii))
    except ZeroDivisionError as e:
        #print("wrong: i={} {}".format(iii,e.message))
        print("wrong: i={} {}".format(iii,"nooooooo"))
    #else:
    #    print("OK")
    finally:
        print("continue...")

def pickkey(mylist):
    """ jg's function"""
    return mylist[1]


quit()








#listjg=[ (5,'A'), (4,'Z'), (8,'N'), (2,'C'), ]
#listjg.sort(key=pickkey) ;print(listjg)
#listjg.sort(reverse=True) ;print(listjg)
quit()

x=3

#def myfL(a,b):
#   return []

def myf (a,b,*other):
    print(type(other))
    print(sum(other))
    c=sum(other)
    #return (a+b+other)

#res=myf(5,2,1) ;print(res)
#res=myf(a=5,b=2,c=1) ;print(res)
#res=myf(b=2,a=5,c=1) ;print(res)
#res=myf(a=5) ;print(res)

#no res=myf(a=5,b=2,c=1) ;print(res)
#res=myf(5,2,1,0) ;print(res)

#myf(5,2)

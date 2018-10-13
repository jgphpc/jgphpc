#!/usr/bin/env python

def myf (a,b):
    return (a+6*a*b-a*b*b)
    #return (a+b*(6*a-a*b))

res=myf(4,-6); print(res)
res=myf(-3,5); print(res)

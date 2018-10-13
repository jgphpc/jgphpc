#!/bin/bash

timestamp=$1    # 2016/10/06-00:46:29
# convert timestamp to epoch
year=`echo $timestamp|awk '{print substr($0,1,4)}'`
month=`echo $timestamp|awk '{print substr($0,6,2)}'`
day=`echo $timestamp|awk '{print substr($0,9,2)}'`
hour=`echo $timestamp|awk '{print substr($0,12,2)}'`
min=`echo $timestamp|awk '{print substr($0,15,2)}'`
sec=`echo $timestamp|awk '{print substr($0,18,2)}'`
epoch=`echo $year $month $day $hour $min $sec |awk '{print mktime(sprintf("%d %d %d %d %d %d", $1,$2,$3,$4,$5,$6)) }'`

echo "$epoch @ $timestamp @"

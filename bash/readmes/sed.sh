#!/bin/bash

in=$1
# 1 AJ AK CB EK GLR JB JF JG JO LM MKr RS SK SO TM TR VH WS

while read line ;do
    fname=`echo "$line" |cut -d: -f1 |xargs basename`
    name1=`echo "$line" |cut -d: -f3 |cut -d= -f2 |sed -e "s/\[//" -e "s/]//" -e "s/'//g" -e "s/,//" |awk '{print $1}'`
    name2=`echo "$line" |cut -d: -f3 |cut -d= -f2 |sed -e "s/\[//" -e "s/]//" -e "s/'//g" -e "s/,//" |awk '{print $2}'`
    # echo "$fname $name1 $name2"
    x=
    if [ "$name1" = "1" ] ;then x="${x}1" ;else x="${x}0" ;fi
    if [ "$name1" = "AJ" ] ;then x="${x}1" ;else x="${x}0" ;fi
    if [ "$name1" = "AK" ] ;then x="${x}1" ;else x="${x}0" ;fi
    if [ "$name1" = "CB" ] ;then x="${x}1" ;else x="${x}0" ;fi
    if [ "$name1" = "EK" ] ;then x="${x}1" ;else x="${x}0" ;fi
    if [ "$name1" = "GLR" ] ;then x="${x}1" ;else x="${x}0" ;fi
    if [ "$name1" = "JB" ] ;then x="${x}1" ;else x="${x}0" ;fi
    if [ "$name1" = "JF" ] ;then x="${x}1" ;else x="${x}0" ;fi
    if [ "$name1" = "JG" ] ;then x="${x}1" ;else x="${x}0" ;fi
    if [ "$name1" = "JO" ] ;then x="${x}1" ;else x="${x}0" ;fi
    if [ "$name1" = "LM" ] ;then x="${x}1" ;else x="${x}0" ;fi
    if [ "$name1" = "MKr" ] ;then x="${x}1" ;else x="${x}0" ;fi
    if [ "$name1" = "RS" ] ;then x="${x}1" ;else x="${x}0" ;fi
    if [ "$name1" = "SK" ] ;then x="${x}1" ;else x="${x}0" ;fi
    if [ "$name1" = "SO" ] ;then x="${x}1" ;else x="${x}0" ;fi
    if [ "$name1" = "TM" ] ;then x="${x}1" ;else x="${x}0" ;fi
    if [ "$name1" = "TR" ] ;then x="${x}1" ;else x="${x}0" ;fi
    if [ "$name1" = "VH" ] ;then x="${x}1" ;else x="${x}0" ;fi
    if [ "$name1" = "WS" ] ;then x="${x}1" ;else x="${x}0" ;fi
    # echo $x
    if [ "$name2" = "1" ]   ;then y=`echo $x |sed -r 's/^()./\11/'` ;fi
    if [ "$name2" = "AJ" ]  ;then y=`echo $x |sed -r 's/^(.)./\11/'` ;fi
    if [ "$name2" = "AK" ]  ;then y=`echo $x |sed -r 's/^(..)./\11/'` ;fi
    if [ "$name2" = "CB" ]  ;then y=`echo $x |sed -r 's/^(...)./\11/'` ;fi
    if [ "$name2" = "EK" ]  ;then y=`echo $x |sed -r 's/^(....)./\11/'` ;fi
    if [ "$name2" = "GLR" ] ;then y=`echo $x |sed -r 's/^(.....)./\11/'` ;fi
    if [ "$name2" = "JB" ]  ;then y=`echo $x |sed -r 's/^(......)./\11/'` ;fi
    if [ "$name2" = "JF" ]  ;then y=`echo $x |sed -r 's/^(.......)./\11/'` ;fi
    if [ "$name2" = "JG" ]  ;then y=`echo $x |sed -r 's/^(........)./\11/'` ;fi
    if [ "$name2" = "JO" ]  ;then y=`echo $x |sed -r 's/^(.........)./\11/'` ;fi
    if [ "$name2" = "LM" ]  ;then y=`echo $x |sed -r 's/^(..........)./\11/'` ;fi
    if [ "$name2" = "MKr" ] ;then y=`echo $x |sed -r 's/^(...........)./\11/'` ;fi
    if [ "$name2" = "RS" ]  ;then y=`echo $x |sed -r 's/^(............)./\11/'` ;fi
    if [ "$name2" = "SK" ]  ;then y=`echo $x |sed -r 's/^(.............)./\11/'` ;fi
    if [ "$name2" = "SO" ]  ;then y=`echo $x |sed -r 's/^(..............)./\11/'` ;fi
    if [ "$name2" = "TM" ]  ;then y=`echo $x |sed -r 's/^(...............)./\11/'` ;fi
    if [ "$name2" = "TR" ]  ;then y=`echo $x |sed -r 's/^(................)./\11/'` ;fi
    if [ "$name2" = "VH" ]  ;then y=`echo $x |sed -r 's/^(.................)./\11/'` ;fi
    if [ "$name2" = "WS" ]  ;then y=`echo $x |sed -r 's/^(..................)./\11/'` ;fi
    yy=`echo $y |sed -e "s/0/0 /g" -e "s/1/1 /g"`
    echo "$fname $yy"
done < $in         

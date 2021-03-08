#!/bin/bash

os=`uname -s`
if [ $os == "Darwin" ] ;then
    echo "script must be on Linux: os=$os"
    exit 0
fi

# ---- usage
function usage {
        cat << EOF
USAGE : arg1=input-type (h=hexa=0x20=20 / b=binary=00100000 / d=decimal=32)
        arg2=number
$0 d 32
        dec=32 dec=32
        dec=32 bin=00100000
        dec=32 hex=0x20
$0 h 20
        hex=20 dec=32
        hex=20 bin=00100000
        hex=20 hex=0x20
$0 b 00100000
        bin=00100000 dec=32
        bin=00100000 bin=00100000
        bin=00100000 hex=0x20
EOF
exit 0
}
if [ $# -lt 2 ] ; then 
        usage
fi

# ---- input parameters
key=$1 # h=hexa / b=binary / d=decimal
in=$2

# ------------------------------------------
# decimal:
# ---- d2d
function d2d {
        printf "dec=%s dec=%s\n" "$1" "$1"
}
# ---- d2b
function d2b {
        # always put obase first !
        tmp=`echo "obase=2;ibase=10;$1" |bc -l`
        pu=`printf "%08d\n" "$tmp" |rev|sed -e "s-0-\n0-g" -e "s-1-\n1-g" |awk 'BEGIN{printf "[ "}$0==1{printf "%s ",NR-2}END{printf "]"}'`
        printf "dec=%s bin=%08d pu=%s\n" "$1" "$tmp" "$pu"

        #ok echo $1 |awk '{r="";a=$1;while(a){r=a%2r;a=int(a/2)} printf"dec=%s bin=%08d\n", $0,r}'
        #ok # http://stackoverflow.com/questions/18870209/convert-a-decimal-number-to-hexadecimal-and-binary-in-a-shell-script

        #ok D2B=({0..1}{0..1}{0..1}{0..1}{0..1}{0..1}{0..1}{0..1})
        #ok echo tmp=${D2B[$1]}
        # http://stackoverflow.com/questions/10278513/bash-shell-decimal-to-binary-conversion
}
# ---- d2h
function d2h {
        echo $1 |awk '{printf"dec=%s hex=0x%02x\n", $0,$0}'
}
# ------------------------------------------

# ------------------------------------------
# binary:
## ---- b2d
function b2d {
        #ko! tmp=`echo "ibase=2;obase=10;$1" |bc -l`
        tmp=`echo "obase=10;ibase=2;$1" |bc -l`
        printf "bin=%s dec=%s\n" "$1" "$tmp"
}
## ---- b2b
function b2b {
        pu=`printf "%s\n" "$1" |rev|sed -e "s-0-\n0-g" -e "s-1-\n1-g" |awk 'BEGIN{printf "[ "}$0==1{printf "%s ",NR-2}END{printf "]"}'`
        printf "bin=%s bin=%s pu=%s\n" "$1" "$1" "$pu"
}
## ---- b2h
function b2h {
        # always put obase first !
        tmp=`echo "obase=16;ibase=2;$1" |bc -l`
        printf "bin=%s hex=0x%s\n" "$1" "$tmp"
}
# ------------------------------------------


# ------------------------------------------
# hexadecimal:
# ---- h2d
function h2d {
        printf "hex=%s dec=%d\n" "$1" "0x$1"
}
# ---- h2b
function h2b {
        # h2b = h2d+d2b
        tmp_h2d=`printf "%d\n" "0x$1"`
        #ok echo "$tmp_h2d" "$1"|awk '{r="";a=$1;while(a){r=a%2r;a=int(a/2)} printf"hex=%s bin=%08d\n", $2,r}'
        hex="$1"
        bin=`echo "$tmp_h2d" |awk '{r="";a=$1;while(a){r=a%2r;a=int(a/2)} printf"%08d", r}'`
        pu=`printf "%s\n" "$bin" |rev|sed -e "s-0-\n0-g" -e "s-1-\n1-g" |awk 'BEGIN{printf "[ "}$0==1{printf "%s ",NR-2}END{printf "]"}'`
        printf "hex=%s bin=%s pu=%s\n" "$hex" "$bin" "$pu"
        #ok echo "$tmp_h2d" "$1"|awk '{r="";a=$1;while(a){r=a%2r;a=int(a/2)} printf"hex=%s bin=%08d\n", $2,r}'        
}
# ---- h2h
function h2h {
        printf "hex=%s hex=0x%s\n" "$1" "$1"
}
# ------------------------------------------


# ------------------------------------------
case "$key" in                                                                                                                        
     d)  d2d $in;d2b $in;d2h $in;;
     b)  b2d $in;b2b $in;b2h $in;;
     h)  h2d $in;h2b $in;h2h $in;;
     *)  usage;;
esac


#!/bin/bash

# for i in `seq 0 127`;do ./0.sh $i ;done
#   phy_core=0 log_core=128 pu=[ 0 128 ] hex_=0x100000000000000000000000000000001
#   phy_core=1 log_core=129 pu=[ 1 129 ] hex_=0x200000000000000000000000000000002
#   phy_core=2 log_core=130 pu=[ 2 130 ] hex_=0x400000000000000000000000000000004

# {{{ cores
function core_level(){
    phy_core=$1
    # log_core=$2
    cores_per_socket=128
    log_core=`expr $phy_core + $cores_per_socket`
    echo -n "phy_core=$phy_core log_core=$log_core "

    x=$(for c in `seq 0 255` ;do
        if [ $c -eq $phy_core ] ;then
            echo -n 1
        elif [ $c -eq $log_core ] ;then
            echo -n 1
        else
            echo -n 0
        fi
    done |rev)

    # echo $x
    ./hexa_binary_decimal_converter.sh b $x
}
# }}}

# {{{ numa domains
function numa_level(){
    if [ $1 -eq 0 ] ;then
        numa="0 128 1 129 2 130 3 131 4 132 5 133 6 134 7 135 8 136 9 137 10 138 11 139 12 140 13 141 14 142 15 143"
    elif [ $1 -eq 1 ] ;then
        numa="16 144 17 145 18 146 19 147 20 148 21 149 22 150 23 151 24 152 25 153 26 154 27 155 28 156 29 157 30 158 31 159"
    elif [ $1 -eq 2 ] ;then
        numa="32 160 33 161 34 162 35 163 36 164 37 165 38 166 39 167 40 168 41 169 42 170 43 171 44 172 45 173 46 174 47 175"
    elif [ $1 -eq 3 ] ;then
        numa="48 176 49 177 50 178 51 179 52 180 53 181 54 182 55 183 56 184 57 185 58 186 59 187 60 188 61 189 62 190 63 191"
    elif [ $1 -eq 4 ] ;then
        numa="64 192 65 193 66 194 67 195 68 196 69 197 70 198 71 199 72 200 73 201 74 202 75 203 76 204 77 205 78 206 79 207"
    elif [ $1 -eq 5 ] ;then
        numa="80 208 81 209 82 210 83 211 84 212 85 213 86 214 87 215 88 216 89 217 90 218 91 219 92 220 93 221 94 222 95 223"
    elif [ $1 -eq 6 ] ;then
        numa="96 224 97 225 98 226 99 227 100 228 101 229 102 230 103 231 104 232 105 233 106 234 107 235 108 236 109 237 110 238 111 239"
    elif [ $1 -eq 7 ] ;then
        numa="112 240 113 241 114 242 115 243 116 244 117 245 118 246 119 247 120 248 121 249 122 250 123 251 124 252 125 253 126 254 127 255"
    else
        echo "unknown numa: $1"
    fi

    x=$(for c in `seq 0 255` ;do
            found=F
            for cc in $numa; do
                if [ $c -eq $cc ] ;then
                    found=T
                fi
            done
            if [ $found == T ] ;then
                echo -n 1
            else
                echo -n 0
            fi
    done |rev)
    echo $x
    ./hexa_binary_decimal_converter.sh b $x
}
# }}}



# {{{ sockets
function socket_level(){
    if [ $1 -eq 0 ] ;then
        socket="0 128 1 129 2 130 3 131 4 132 5 133 6 134 7 135 8 136 9 137 10 138 11 139 12 140 13 141 14 142 15 143 16 144 17 145 18 146 19 147 20 148 21 149 22 150 23 151 24 152 25 153 26 154 27 155 28 156 29 157 30 158 31 159 32 160 33 161 34 162 35 163 36 164 37 165 38 166 39 167 40 168 41 169 42 170 43 171 44 172 45 173 46 174 47 175 48 176 49 177 50 178 51 179 52 180 53 181 54 182 55 183 56 184 57 185 58 186 59 187 60 188 61 189 62 190 63 191"
    elif [ $1 -eq 1 ] ;then
        socket="64 192 65 193 66 194 67 195 68 196 69 197 70 198 71 199 72 200 73 201 74 202 75 203 76 204 77 205 78 206 79 207 80 208 81 209 82 210 83 211 84 212 85 213 86 214 87 215 88 216 89 217 90 218 91 219 92 220 93 221 94 222 95 223 96 224 97 225 98 226 99 227 100 228 101 229 102 230 103 231 104 232 105 233 106 234 107 235 108 236 109 237 110 238 111 239 112 240 113 241 114 242 115 243 116 244 117 245 118 246 119 247 120 248 121 249 122 250 123 251 124 252 125 253 126 254 127 255"
    else
        echo "unknown socket: $1"
    fi

    x=$(for c in `seq 0 255` ;do
            found=F
            for cc in $socket; do
                if [ $c -eq $cc ] ;then
                    found=T
                fi
            done
            if [ $found == T ] ;then
                echo -n 1
            else
                echo -n 0
            fi
    done |rev)
    echo $x
    ./hexa_binary_decimal_converter.sh b $x
}

# core_level $1 $2
# numa_level $1
socket_level $1

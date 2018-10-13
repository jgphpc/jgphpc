#include <stdio.h>
#include <pmi.h>

// CASE #168800
// cc ./1.c -o s
//
// cc -dynamic 1.c
// /opt/cray/pe/cce/8.5.5/cray-binutils/x86_64-pc-linux-gnu/bin/ld: /tmp/pe_126328/1_1.o: undefined reference to symbol 'PMI_Get_nid'
//
// cc -dynamic ./1.c $CRAY_PMI_POST_LINK_OPTS -lpmi -o d
// export PE_PKGCONFIG_LIBS=cray-pmi:cray-ugni:$PE_PKGCONFIG_LIBS
// export PMI_VERSION_DISPLAY=1
// srun -n1 -C gpu ./a.out
// Thu May 11 17:48:41 2017: [PE_0]: PMI VERSION  : version 5.0.11
// PMI BUILD INFO  : Built Mon Dec 05 11:10:48 2016 (git hash 79adf9a)
// pmi/5.0.10-1.0000.11050.0.0.ari
// nmm /opt/cray/pe/pmi/5.0.10-1.0000.11050.0.0.ari/lib64/libpmi.a  |grep "T "|grep CRAY
// 0000000000000000 T PMI_CRAY_Get_base_rank_in_app
// 0000000000000000 T PMI_CRAY_Get_app_size
// 0000000000000000 T PMI_CRAY_Get_num_apps
// 0000000000000000 T PMI_CRAY_Get_rank_in_app
// 0000000000000000 T PMI_CRAY_gethostbyname
// nm s |grep PMI_CRAY_
// 00000000004d61ac T PMI_CRAY_Get_app_size
// 00000000004d621c T PMI_CRAY_Get_num_apps
// 00000000004d6270 T PMI_CRAY_Get_rank_in_app
// 0000000000421bd0 T PMI_CRAY_gethostbyname
int main() {
    int nid;
    PMI_Get_nid(0, &nid);
    printf("nid=%d\n",nid);
    return 0;
}

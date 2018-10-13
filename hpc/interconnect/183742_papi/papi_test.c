#define _GNU_SOURCE
#include <papi.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <math.h>
#include <mpi.h>
#include <sched.h>
#include <rca_lib.h>

// Aries counters
// One counter per nic
char *nic_counters[] = {
  "cray_npu:::AR_NIC_NETMON_ORB_EVENT_CNTR_REQ_PKTS",
  "cray_npu:::AR_NIC_NETMON_ORB_EVENT_CNTR_REQ_FLITS",
  "cray_npu:::AR_NIC_NETMON_ORB_EVENT_CNTR_REQ_STALLED",
  "cray_npu:::AR_NIC_NETMON_ORB_EVENT_CNTR_RSP_FLITS",
  "cray_npu:::AR_NIC_NETMON_ORB_EVENT_CNTR_RSP_PKTS",
  "cray_npu:::AR_NIC_NETMON_ORB_EVENT_CNTR_RSP_STALLED",
  "cray_npu:::AR_NIC_NETMON_ORB_EVENT_CNTR_RSP_BLOCKED",
  NULL
};
// 5x8 counters - One counter per tile for rows 0-4
// Format: AR_RTR_r_c_* (r is row number, c is column number)
char *tile_counters[] = {"INQ_PRF_ROWBUS_STALL_CNT",
			 "INQ_PRF_ROWBUS_2X_USAGE_CNT",
			 "INQ_PRF_PKT_TO_DEAD_LINK_CNT",
			 "COLBUF_PERF_STALL_RQ:COL_BUF_PERF_STALL_RQ",
			 "COLBUF_PERF_STALL_RS:COL_BUF_PERF_STALL_RS",
			 "COLBUF_PERF_STALL_RQ:VC_PTR",
			 "COLBUF_PERF_STALL_RS:VC_PTR",
			 NULL};
// 1x8 counters - One counter per tile for row 5
// Format: AR_RTR_PT_5_c_* (r is row number, c is column number)
char *tile_counters_pt[] = {"INQ_PRF_REQ_ROWBUS_STALL_CNT",
			    "INQ_PRF_RSP_ROWBUS_STALL_CNT",
			    "INQ_PRF_ROWBUS_2X_USAGE_CNT",
			    "INQ_PRF_PKT_TO_DEAD_LINK_CNT",
			    "COLBUF_PERF_STALL_RQ",
			    "COLBUF_PERF_STALL_RS",
			    "INQ_PRF_INCOMING_FLIT_VC0",
			    "INQ_PRF_INCOMING_FLIT_VC4",
			    NULL};

// 5x8 counters - One counter per tile per VC for rows 0-4
// Format: AR_RTR_r_c_*_VC*
char *tile_counters_vc[] = {"INQ_PRF_INCOMING_FLIT",
			    NULL};

#define NUM_TILE_ROWS 5
#define NUM_TILE_COLS 8
#define NUM_TILE_VCS  8

#define XMAX   19
#define YMAX    6
#define ZMAX   16
#define HMAX    4
#define NLINKS 48

#define PAPI_CHKERR(err) \
  if(err!=PAPI_OK) { \
    if(rank==0) printf("PAPI error %d: %s\n",err,PAPI_strerror(err));	\
  }

int main(int argc, char *argv[])
{
  int i, j, k, code=0, cidx, nctrs, rank, size, err, cpu;
  int papi_rank=1, nevents=0, event_set=PAPI_NULL;
  long long *values;
  FILE *fp;

  // Init MPI
  MPI_Init(&argc,&argv);
  MPI_Comm_rank(MPI_COMM_WORLD,&rank);
  MPI_Comm_size(MPI_COMM_WORLD,&size);
  if(rank==0) printf("Starting Papi Test on %d cores\n",size);

  // Get my cpu
  cpu = sched_getcpu();
  papi_rank = (cpu == 0);
  printf("rank=%d cpu=%d papi_rank=%d\n",rank,cpu,papi_rank);
  
  // Init PAPI on one core per node
  if(papi_rank) PAPI_library_init(PAPI_VER_CURRENT);
  
  if(rank==0) printf("Setting up rd event set\n");

  if(papi_rank) {
    // Create PAPI event set
    err = PAPI_create_eventset(&event_set);PAPI_CHKERR(err);
    
    // Add nic counters
    for (i=0; nic_counters[i] != NULL; i++) {
      printf("rank=%d adding nic counter %s\n",rank,nic_counters[i]);
      err = PAPI_add_named_event(event_set,nic_counters[i]);PAPI_CHKERR(err);
      nevents++;
    }

    // Add tile counters
    for (i=0; tile_counters[i] != NULL; i++) {
      for(j=0; j<NUM_TILE_ROWS; j++) {
	for(k=0; k<NUM_TILE_COLS; k++) {
	  char tile_counter[200];
	  sprintf(tile_counter,"cray_npu:::AR_RTR_%d_%d_%s",j,k,tile_counters[i]);
	  printf("rank=%d adding tile counter %s\n",rank,tile_counter);
	  err = PAPI_add_named_event(event_set,tile_counter);PAPI_CHKERR(err);
	  nevents++;
	}
      }
    }

    // Add processor tile counters
    for (i=0; tile_counters_pt[i] != NULL; i++) {
      for(k=0; k<NUM_TILE_COLS; k++) {
	char tile_counter[200];
	sprintf(tile_counter,"cray_npu:::AR_RTR_PT_5_%d_%s",k,tile_counters_pt[i]);
	printf("rank=%d adding pt tile counter %s\n",rank,tile_counter);
	err = PAPI_add_named_event(event_set,tile_counter);PAPI_CHKERR(err);
	nevents++;
      }
    }
    
    // Add tile counters for virtual channels
    int l;
    for (i=0; tile_counters_vc[i] != NULL; i++) {
      for(j=0; j<NUM_TILE_ROWS; j++) {
	for(k=0; k<NUM_TILE_COLS; k++) {
	  for(l=0; l<NUM_TILE_VCS; l++) {
	    char tile_counter[200];
	    sprintf(tile_counter,"cray_npu:::AR_RTR_%d_%d_%s_VC%d",j,k,tile_counters_vc[i],l);
	    printf("rank=%d adding vc tile counter %s\n",rank,tile_counter);
	    err = PAPI_add_named_event(event_set,tile_counter);PAPI_CHKERR(err);
	    nevents++;
	  }
	}
      }
    }
  }

  // Read interconnect data
  int              x, y, z, h;
  rca_mesh_coord_t coord;
  rs_node_t        nodeid;
  char             nodestr[200];

  // Get node id
  if(rank==0) printf("Getting node information\n");
  rca_get_nodeid(&nodeid);

  // Extract data from node id
  int row,col,cage,slot,module,link,socket,die,core,nid,isgem,isaries;
  row     = rs_get_row(nodeid);
  col     = rs_get_column(nodeid);
  cage    = rs_get_cage(nodeid);
  slot    = rs_get_slot(nodeid);
  module  = rs_get_module(nodeid);
  link    = rs_get_link(nodeid);
  socket  = rs_get_socket(nodeid);
  die     = rs_get_die(nodeid);
  core    = rs_get_core(nodeid);
  nid     = rs_get_nid(nodeid);
  isgem   = rs_is_gemini(nodeid);
  isaries = rs_is_aries(nodeid);
  int module2 = (int)floor(module/HMAX);
  rca_get_meshcoord(nid, &coord);
  rs_phys2str(&nodeid,nodestr);
    
  x = coord.mesh_x; y = coord.mesh_y;
  z = coord.mesh_z; h = module;

  if(papi_rank) {
    printf("rank=%d x=%d y=%d z=%d h=%d gem=%d aries=%d nodestr=%s row=%d col=%d cage=%d slot=%d module=%d module2=%d "
   	   "link=%d socket=%d die=%d core=%d nid=%d\n",rank,x,y,z,h,isgem,isaries,nodestr,row,col,
	   cage,slot,module,module2,link,socket,die,core,nid);

    // Open interconnect bin file
    fp = fopen("interconnect.bin","rb");

    // Seek to location with info for this node
    int seeksize = (x*YMAX*ZMAX*NLINKS + y*ZMAX*NLINKS + z*NLINKS) * 9;
    fseek(fp,seeksize,SEEK_SET);

    // Read data
    char buf[NLINKS*9];
    fread(buf,NLINKS*9,sizeof(char),fp);

    // Close file
    fclose(fp);

    // Unpack data
    printf("rank=%d unpacking data\n",rank);
    int data[6][8][9];
    int i,d,l;
    for(i=0; i<NLINKS; i++) {
      d = i*9;
      l = buf[d+3];
      int xlink = floor(l/10);
      int ylink = l % 10;
      data[xlink][ylink][0] = buf[d];
      data[xlink][ylink][1] = buf[d+1];
      data[xlink][ylink][2] = buf[d+2];
      data[xlink][ylink][3] = buf[d+3];
      data[xlink][ylink][4] = buf[d+4];
      data[xlink][ylink][5] = buf[d+5];
      data[xlink][ylink][6] = buf[d+6];
      data[xlink][ylink][7] = buf[d+7];
      data[xlink][ylink][8] = buf[d+8];
      printf("rank=%d buf=%d %d %d %d %d %d %d %d %d\n",
	     rank,data[xlink][ylink][0],data[xlink][ylink][1],
	     data[xlink][ylink][2],data[xlink][ylink][3],
	     data[xlink][ylink][4],data[xlink][ylink][5],
	     data[xlink][ylink][6],data[xlink][ylink][7],
	     data[xlink][ylink][8]);
    }
  }

  MPI_Barrier(MPI_COMM_WORLD);
  if(rank==0) printf("Performing work\n\n");
  MPI_Barrier(MPI_COMM_WORLD);

  if(papi_rank) {
    // Start counters
    err = PAPI_start(event_set);PAPI_CHKERR(err);
  }

  // Perform on-node work
  values = (long long*)malloc(sizeof(long long)*nevents);
  memset(values, 0, sizeof(long long)*nevents);

  // Perform comm work
  int ntests = 10000;
  for(i=0; i<ntests; i++) {
    int sval = rank, rval = -1;
    MPI_Allreduce(&sval,&rval,1,MPI_INT,MPI_SUM,MPI_COMM_WORLD);
  }
  
  // Wait for comm to finish
  MPI_Barrier(MPI_COMM_WORLD);

  if(papi_rank) {
    // Stop counters and get results
    err = PAPI_stop(event_set, values);PAPI_CHKERR(err);

    // Print nic counters
    int ind = 0;
    for(i=0; nic_counters[i]!=NULL; i++) {
      printf("rank=%d nic counter %s = %lld\n", rank, nic_counters[i], values[ind]);
      ind++;
    }

    // Print tile counters
    for (i=0; tile_counters[i] != NULL; i++) {
      for(j=0; j<NUM_TILE_ROWS; j++) {
	for(k=0; k<NUM_TILE_COLS; k++) {
	  char tile_counter[100];
	  sprintf(tile_counter,"cray_npu:::AR_RTR_%d_%d_%s",j,k,tile_counters[i]);
	  printf("rank=%d tile counter %s = %lld\n", rank, tile_counter, values[ind]);
	  ind++;
	}
      }
    }
    
    // Print processor tile counters
    for (i=0; tile_counters_pt[i] != NULL; i++) {
      for(k=0; k<NUM_TILE_COLS; k++) {
	char tile_counter[200];
	sprintf(tile_counter,"cray_npu:::AR_RTR_PT_5_%d_%s",k,tile_counters_pt[i]);
	printf("rank=%d pt tile counter %s = %lld\n", rank, tile_counter, values[ind]);
	ind++;
      }
    }
    
    // Print tile counters for virtual channels
    for (i=0; tile_counters_vc[i] != NULL; i++) {
      for(j=0; j<NUM_TILE_ROWS; j++) {
	for(k=0; k<NUM_TILE_COLS; k++) {
	  long long sumvcs = 0;
	  for(int l=0; l<NUM_TILE_VCS; l++) {
	    sumvcs += values[ind];
	    ind++;
	  }
	  char tile_counter[200];
	  sprintf(tile_counter,"AR_RTR_%d_%d_%s_VCS",j,k,tile_counters_vc[i]);
	  printf("rank=%d vc tile counter %s = %lld\n", rank, tile_counter, sumvcs);
	}
      }
    }

    // Cleanup and destroy PAPI
    printf("Destroying PAPI\n");
    err = PAPI_cleanup_eventset(event_set);PAPI_CHKERR(err);
    err = PAPI_destroy_eventset(&event_set);PAPI_CHKERR(err);
    PAPI_shutdown();
  }

  // End test
  MPI_Barrier(MPI_COMM_WORLD);
  if(rank==0) printf("Done with Papi Test\n");
  free(values);
  MPI_Finalize();
  return 0;
}

from mpi4py import MPI;
from vsc.mympingpong.pingpongers import PingPongSR
from vsc.utils.generaloption import simple_option

# srun -Cgpu -t1 -n2 -c1 --ntasks-per-core=1 python ./2.py

_basic = [-7,]
# _basic = [-7, 0, 7,]
# _basic = [None,
#           True, False,
#           -7, 0, 7,
#           -2**63+1, 2**63-1,
#           -2.17, 0.0, 3.14,
#           1+2j, 2-3j,
#           'mpi4py',
#           ]
messages = list(_basic)

COMM = MPI.COMM_WORLD
size = COMM.Get_size()
rank = COMM.Get_rank()    
#print ('### %d/%d' % (rank, size) )

#log = logger
#pp = PingPongSR.pingpongfactory('SR' + 'fast', COMM, rank+1, log)

for smess in messages:
    if rank == 0:
        COMM.send(smess,  rank+1, 0)
        rmess = smess
    else:
        rmess = COMM.recv(None, rank-1, 0)
    print ('### %d: %d' % (rank, rmess) )
    #print (Comm)
# PingpongSR(self, rbuf ,sbuf, rsource=0 ,sdest=1 ,rtag=0 ,stag=0, num=1, rstatus)
# PingpongSR(self,rmess,smess,0,1,0,0,1,rstatus)

    #COMM.send(smess,  COMM)
    #rmess = COMM.recv(None, COMM, 0)


#    assertEqual(rmess, None)
#      if size == 1: return
#      for smess in messages:
#          if rank == 0:
#              self.COMM.send(smess,  rank+1, 0)
#              rmess = smess
#          elif rank == size - 1:
#              rmess = self.COMM.recv(None, rank-1, 0)
#          else:
#              rmess = self.COMM.recv(None, rank-1, 0)
#              self.COMM.send(rmess,  rank+1, 0)
#          self.assertEqual(rmess, smess)

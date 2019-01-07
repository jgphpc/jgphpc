"""A very simple example to help benchmark PySPH. (2 minutes)

The example creates a cube shaped block of water falling in free-space under
the influence of gravity while solving the incompressible, inviscid flow
equations.  Only 5 time steps are solved but with a million particles.  It is
easy to change the number of particles by simply passing the command line
argument --np to a desired number::

    $ pysph run cube --np 2e6

To check the performance of PySPH using OpenMP one could try the following::

    $ pysph run cube --disable-output

    $ pysph run cube --disable-output --openmp

"""

import cProfile, sys # cscs: cProfile

from mpi4py import MPI
import os
import psutil

import numpy

from pysph.base.kernels import CubicSpline
from pysph.base.utils import get_particle_array_wcsph
from pysph.solver.application import Application
from pysph.sph.scheme import WCSPHScheme

rho0 = 1000.0


class Cube(Application):
    def add_user_options(self, group):
        group.add_argument(
            "--np", action="store", type=float, dest="np", default=int(1e5),
            help="Number of particles in the cube (1e5 by default)."
        )

    def consume_user_options(self):
        self.hdx = 1.5
        self.dx = 1.0/pow(self.options.np, 1.0/3.0)

    def configure_scheme(self):
        self.scheme.configure(h0=self.hdx*self.dx, hdx=self.hdx)
        kernel = CubicSpline(dim=3)
        dt = 1e-4
        tf = 5e-4
        self.scheme.configure_solver(kernel=kernel, tf=tf, dt=dt)

    def create_scheme(self):
        co = 10.0
        s = WCSPHScheme(
            ['fluid'], [], dim=3, rho0=rho0, c0=co,
            h0=0.1, hdx=1.5, gz=-9.81, gamma=7.0,
            alpha=0.5, beta=0.0
        )
        return s

    def create_particles(self):
        dx = self.dx
        hdx = self.hdx
        xmin, xmax = 0.0, 1.0
        ymin, ymax = 0.0, 1.0
        zmin, zmax = 0.0, 1.0
        x, y, z = numpy.mgrid[xmin:xmax:dx, ymin:ymax:dx, zmin:zmax:dx]
        x = x.ravel()
        y = y.ravel()
        z = z.ravel()

        # set up particle properties
        h0 = hdx * dx

        volume = dx**3
        m0 = rho0 * volume

        fluid = get_particle_array_wcsph(name='fluid', x=x, y=y, z=z)
        fluid.m[:] = m0
        fluid.h[:] = h0

        fluid.rho[:] = rho0
        #nnps = LinkedListNNPS(dim=3, particles=[fluid])
        #nnps.spatially_order_particles(0)

        print("Number of particles:", x.size)
        fluid.set_lb_props( list(fluid.properties.keys()) )
        return [fluid]


if __name__ == '__main__':
    cscs_size = MPI.COMM_WORLD.Get_size()
    cscs_rank = MPI.COMM_WORLD.Get_rank()
    cscs_name = MPI.Get_processor_name()
    cscs_core = os.sched_getaffinity(psutil.Process().pid)
    sys.stdout.write(
        "#CSCS: rank= %d /%d cn=%s c=%s\n"
        % (cscs_rank, cscs_size, cscs_name, cscs_core))

    # --- cProfile:
    pr = cProfile.Profile()                  # cscs: cProfile 
    pr.enable()                              # cscs: cProfile
    app = Cube()
    app.run()
    pr.disable()                             # cscs: cProfile
    pr.dump_stats('cpu_%d.cprofile' % cscs_rank) # cscs: cProfile (binary dump)

    #with open( 'cpu_%d.txt' %comm.rank, 'w') as output_file:
    #    sys.stdout = output_file
    #    pr.print_stats( sort='time' )   # cscs: cProfile (text dump)
    #    sys.stdout = sys.__stdout__

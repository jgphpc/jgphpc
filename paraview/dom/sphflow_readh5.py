#   With the conflicts between the different python modules being resolved, I
#   can now load your data directly using h5py, instead of using XDMF. This
#   gives the opportunity to do sub-sampling very easily, using numpy array
#   slicing, and it also gives the opportunity to distribute very large
#   particles sets among multiple processors (using again the numpy array
#   slicing).
#   an example to be used in a Programmable Source would be:

import h5py
file = h5py.File("/scratch/snx3000tds/piccinal/sphflow/rotating_square_patch_3D/015/RES/square109.h5", "r")

x= file["Fluid#0"]['X']
y= file["Fluid#0"]['Y']
z= file["Fluid#0"]['Z']
output.Points = make_vector(x,y,z)

vx= file["Fluid#0"]['VX']
vy= file["Fluid#0"]['VY']
vz= file["Fluid#0"]['VZ']
output.PointData.append(make_vector(vx,vy,vz), "Velocity")

P=file["Fluid#0"]['P'][()]
output.PointData.append(P, "P")

file.close()

nnodes = output.GetNumberOfPoints()
ptIds = vtk.vtkIdList()
ptIds.SetNumberOfIds(nnodes)

for a in range(nnodes):
  ptIds.SetId(a , a)

output.Allocate(1)
output.InsertNextCell(vtk.VTK_POLY_VERTEX , ptIds)


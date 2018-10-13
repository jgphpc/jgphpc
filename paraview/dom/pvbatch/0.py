from paraview.simple import *

#reader = XDMFReader(FileNames=['/scratch/snx3000tds/piccinal/sphflow/rotating_square_patch_3D/015/RES/square200.h5.xmf'])
reader = XDMFReader(FileNames=['/scratch/snx3000tds/piccinal/sphflow/rotating_square_patch_3D/015/RES/square278.h5.xmf'])

reader.PointArrayStatus = ['DeltaX', 'ID', 'Interface', 'Kind', 'Marker', 'P', 'Velocity', 'Volume']

reader.GridStatus = ['Particles']

rep=Show()

rep.SetRepresentationType("Points")

ResetCamera()

SaveScreenshot("foo.png")


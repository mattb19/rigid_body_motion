
# import the required modules
import math
import numpy as np
import rpm

# define theta
theta = math.pi/2

# define vector
v0 = rpm.vec(1,1,0)

# create rotations
Rx = rpm.rot_x(theta)
Ry = rpm.rot_y(theta)
Rz = rpm.rot_z(theta)

# calculate total rotations
R = np.matmul(Rx,Ry)
R1 = np.matmul(R, Rz)

# calculate results
v01 = R1.dot(v0)
print('The transformed vector (CURRENT FRAME) is:\n',v01)
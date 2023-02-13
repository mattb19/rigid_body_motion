# Here we write some functions that help us analayze the motions of a rigid body

# import the required modules
import math
import numpy as np

# first transformation
def trans_x_a(a):
	rot = np.array([[1.0,0.0,0.0,a],
				   [0.0,1.0,0.0,0.0],
				   [0.0,0.0,1.0,0.0],
				   [0.0,0.0,0.0,1.0]])
	return rot


# second transformation
def trans_y_b(b):
	rot = np.array([[1.0,0.0,0.0,0.0],
				   [0.0,1.0,0.0,b],
				   [0.0,0.0,1.0,0.0],
				   [0.0,0.0,0.0,1.0]])
	return rot

# third transformation
def trans_z_c(c):
	rot = np.array([[1.0,0.0,0.0,0.0],
				   [0.0,1.0,0.0,0.0],
				   [0.0,0.0,1.0,c],
				   [0.0,0.0,0.0,1.0]])
	return rot

# fourth transformation
def rot_x_a(a):
	rot = np.array([[1.0,0.0,		0.0,		 0.0],
				   [0.0,math.cos(a),-math.sin(a),0.0],
				   [0.0,math.sin(a),math.cos(a), 0.0],
				   [0.0,0.0,        0.0,		 1.0]])
	return rot

# fifth transformation
def rot_y_b(b):
	rot = np.array([[math.cos(b), 0.0,math.sin(b), 0.0],
				   [0.0,		 1.0,0.0,	 	  0.0],
				   [-math.sin(b),0.0,math.cos(b), 0.0],
				   [0.0,		 0.0,0.0,		  1.0]])
	return rot

# sixth transformation
def rot_x_c(c):
	rot = np.array([[math.cos(c),-math.sin(c),0.0,0.0],
				   [math.sin(c),math.cos(c), 0.0,0.0],
				   [0.0,		    0.0,	 1.0,0.0],
				   [0.0,			0.0,	 0.0,1.0]])
	return rot

# vector
def vec(x,y,z,x1):
#	Define a vector
	vec = np.array([[x, y, z, x1]]).T 
	return vec


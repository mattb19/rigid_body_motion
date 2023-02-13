# import modules
import p2_sol as p2
import math
import numpy as np

def H_1():
	v0 = p2.vec(0,1,1)
	Tx = p2.trans_x_a(2.5)
	Tz = p2.trans_z_c(0.5)
	Ty = p2.trans_y_b(-1.5)
	T = np.matmul(Tx, Tz, Ty)
	v01 = T.dot(v0)
	print('The transformed vector (CURRENT FRAME) is:\n',v01)

def H_2():
	v0 = p2.vec(0,1,1)
	Tz = p2.trans_z_c(-1.5)
	Tx = p2.trans_x_a(2.5)
	Ty = p2.trans_y_b(0.5)
	T = np.matmul(Tz, Tx, Ty)
	v01 = T.dot(v0)
	print('The transformed vector (CURRENT FRAME) is:\n',v01)

def H_3():
	v0 = p2.vec(0,1,1)
	Tx = p2.trans_x_a(2.5)
	Tz = p2.trans_z_c(0.5)
	Ty = p2.trans_y_b(-1.5)
	T = np.matmul(Ty, Tz, Tx)
	v01 = T.dot(v0)
	print('The transformed vector (FIXED FRAME) is:\n',v01)

def H_4():
	v0 = p2.vec(0,1,1)
	Tz = p2.trans_z_c(-1.5)
	Tx = p2.trans_x_a(2.5)
	Ty = p2.trans_y_b(0.5)
	T = np.matmul(Ty, Tx, Tz)
	v01 = T.dot(v0)
	print('The transformed vector (FIXED FRAME) is:\n',v01)

def H_5():
	theta = math.pi/2
	v0 = p2.vec(0,1,1)
	Rx = p2.rot_x_a(theta)
	Tx = p2.trans_x_a(3.0)
	Tz = p2.trans_z_c(-3.0)
	Rz = p2.rot_x_c(-theta)
	TR = np.matmul(Rx, Tx, Tz, Rz)
	v01 = TR.dot(v0)
	print('The transformed vector (CURRENT FRAME) is:\n',v01)



if __name__ == "__main__":
	H_1()
	H_2()
	H_3()
	H_4()
	H_5()

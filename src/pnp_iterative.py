import os
import argparse

import cv2
import numpy as np

parser = argparse.ArgumentParser()
parser.add_argument("input_dir", help="Input directory.")
parser.add_argument("output_dir", help="Output directory.")
args = parser.parse_args()

print 'Using OpenCV ver.',cv2.__version__

# 2D image points from the left camera image
image_points = np.loadtxt(os.path.join(args.input_dir, "image_points.txt"), dtype=float)

# Corresponding 3D raw world points from the laser scan
world_points_raw = np.loadtxt(os.path.join(args.input_dir, "world_points_raw.txt"), dtype=float)

# loading the origin
origin = np.loadtxt(os.path.join(args.input_dir, "origin.txt"), dtype=float)

# the z axis in world points currently contains the absolute elevation ~ 195 m - it needs to be shifted based on the origin 
world_points = world_points_raw - origin

# load camera matrix defined as: 
# [fx 0 cx; 0 fy cy; 0 0 1] 
camera_matrix = np.loadtxt(os.path.join(args.input_dir, "camera_matrix.txt"), dtype=float)
 
dist_coeffs = np.zeros((4,1)) # Assuming no lens distortion - the image points were obtained from a rectified image

# solving the perspective n point projection problem - using the iterative solver
(success, rotation_vector, translation_vector) = cv2.solvePnP(world_points, image_points, camera_matrix, dist_coeffs, flags=cv2.SOLVEPNP_ITERATIVE)

# converting the rotation vector to a rotation matrix
rot_mat, jacobian = cv2.Rodrigues(rotation_vector)

# printing all the parameters
print "Camera Matrix :\n {0}".format(camera_matrix)
print "Rotation Vector:\n {0}".format(rotation_vector)
print "Translation Vector:\n {0}".format(translation_vector)
print "Rotation Matrix: \n {0}".format(rot_mat)

print "saved world_points, rotation matrix and translation matrix text files \n "

np.savetxt(os.path.join(args.output_dir, "rotation_matrix.txt"), rot_mat, fmt='%3.8f', delimiter=' ', newline='\n')
np.savetxt(os.path.join(args.output_dir, "world_points.txt"), rot_mat, fmt='%3.8f', delimiter=' ', newline='\n')
np.savetxt(os.path.join(args.output_dir, "translation_matrix.txt"), translation_vector, fmt='%3.8f', delimiter=' ')
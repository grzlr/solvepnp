#!/usr/bin/env python
 
import cv2
import numpy as np

print 'Using OpenCV ver.',cv2.__version__

# 2D image points from the left camera image
image_points = np.loadtxt("./image_points.txt", dtype=float)

# Corresponding 3D world points from the laser scan
world_points = np.loadtxt("./world_points.txt", dtype=float)

# load camera matrix formatted as 
# [fx 0 cx; 0 fy cy; 0 0 1] 
camera_matrix = np.loadtxt("./camera_matrix.txt", dtype=float)
 
dist_coeffs = np.zeros((4,1)) # Assuming no lens distortion - the image points were obtained from a rectified image

# solving the perspective n point projection problem - using the iterative solver
(success, rotation_vector, translation_vector) = cv2.solvePnP(world_points, image_points, camera_matrix, dist_coeffs, flags=cv2.SOLVEPNP_ITERATIVE)

# converting the rotation vector to a rotation matrix
rot_mat, jacobian = cv2.Rodrigues(rotation_vector)

# printing all the parameters
print "Camera Matrix :\n {0}".format(camera_matrix)
print "Rotation Vector:\n {0}".format(rotation_vector)
print "Translation Vector:\n {0}".format(translation_vector)
print "Rotation Matrix:" 
print(rot_mat)
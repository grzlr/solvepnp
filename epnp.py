#!/usr/bin/env python
 
import cv2
import numpy as np

print 'Using OpenCV ver.',cv2.__version__

# Read Image
# im = cv2.imread("headPose.jpg");
# size = im.shape
     
#2D image points. If you change the image, you need to change vector
image_points = np.array([
                            (999, 692),     # checkboard #1
                            (1338, 934),     # checkboard #2
                            (1109, 411),     # pt on the wall above checkboard
                            (851, 1105)     # pt on the ground below checkboard
                        ], dtype="double")

# Translating the z coordinate cause the laser scanner gives an absolute altitude reading
# Assuming the z coord of the scanner is at 1.5m above ground level. Ground level 
# is assumed to be at 208.8m. So Origin z is 208.8 + 1.5 = 210.3m
model_points = np.array([
                            (2.024243, -2.903477, -0.727078),             # checkboard #1
                            (1.22780, -3.195113, -1.301648),        # checkboard #2
                            (1.823564, -3.115918, -0.034772),     # pt on the wall above checkboard
                            (1.868449, -2.189185, -1.490857)      # pt on the ground below the checkboard
                        ], dtype="double")
 
 
# Camera internals 
focal_length = 1399.53
center = (1169.16, 703.221)
camera_matrix = np.array(
                         [[focal_length, 0, center[0]],
                         [0, focal_length, center[1]],
                         [0, 0, 1]], dtype = "double"
                         )
 
print "Camera Matrix :\n {0}".format(camera_matrix)
 
dist_coeffs = np.zeros((4,1)) # Assuming no lens distortion - the image points were obtained from a rectified image


# Thus, given some data D = np.array(...) where D.shape = (N,M), in order to use a subset of it as,
# e.g., imagePoints, one must effectively copy it into a new array: imagePoints = np.ascontiguousarray(D[:,:2]).reshape((N,1,2))

imagePoints = np.ascontiguousarray(image_points[:,:2]).reshape((4,1,2))
(success, rotation_vector, translation_vector) = cv2.solvePnP(model_points, imagePoints, camera_matrix, dist_coeffs, flags=cv2.SOLVEPNP_EPNP)

rot_mat, jacobian = cv2.Rodrigues(rotation_vector)
 
print "Rotation Vector:\n {0}".format(rotation_vector)
print "Translation Vector:\n {0}".format(translation_vector)
print "Rotation Matrix:" 
print(rot_mat)


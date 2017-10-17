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
                            (851, 1105),     # pt on the ground below checkboard
                            (1333, 690),
                            (997, 936),
                            (1128, 1033),
                            (1374, 1053),
                            (1744, 240),
                            (584, 340)
                        ], dtype="double")
 
# Translating the z coordinate cause the laser scanner gives an absolute altitude reading
# Assuming the z coord of the scanner is at 1.5m above ground level. Origin is at [0, 0, 210.077]. 
world_points = np.array([
                            (2.0242, -2.9035, -0.4348),             # checkboard #1
                            (1.2278, -3.1951, -1.0093),        # checkboard #2
                            (1.8236, -3.1159, 0.2575),     # pt on the wall above checkboard
                            (1.8684, -2.1892, -1.1986),      # pt on the ground below the checkboard
                            (1.3084, -3.3254, -0.4349),
                            (1.9432, -2.7742, -1.0114),
                            (1.5690, -2.7816, -1.1862),
                            (1.0366, -2.9736, -1.1923),
                            (0.4872, -3.8935, 0.6537),
                            (2.9463, -2.4621, 0.4376)
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

(success, rotation_vector, translation_vector) = cv2.solvePnP(world_points, image_points, camera_matrix, dist_coeffs, flags=cv2.SOLVEPNP_ITERATIVE)

rot_mat, jacobian = cv2.Rodrigues(rotation_vector)
 
print "Rotation Vector:\n {0}".format(rotation_vector)
print "Translation Vector:\n {0}".format(translation_vector)
print "Rotation Matrix:" 
print(rot_mat)

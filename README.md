The script automatically performs the 3D point translation w.r.t the user defined origin. Uses the translated points for the pnp solver.

It needs the path input for the input folder and the output folder.

## IO
	Input
	- camera_matrix.txt
		Should have ' ' separated values of the camera intrinsic matrix
	- image_points.txt
		Correspondence points selected from the camera image. Using left camera as default protocol.
	- world_points_raw.txt
		These are the selected correspondence points from the 3D scan. Raw, absolute values.
	- origin.txt
		User defined origin to shift the 3D points along the z-axis. Default 3D scan output is absolute elevation (along z axis that is)
	
	Output
	- world_points.txt
		Translated 3D points
	- rotation_matrix.txt
	- translation_matrix.txt


## flags for solvepnp   

1. SOLVEPNP_ITERATIVE 
	Iterative method is based on Levenberg-Marquardt optimization. In this case, the function finds such a pose that minimizes reprojection error, that is the sum of squared distances between the observed projections imagePoints and the projected (using projectPoints() ) objectPoints.

2. For using P3P or EPNP 
	-The numpy array has to be changed a little. See note at the bottom of the function definition of solvepnp() in: http://docs.opencv.org/3.2.0/d9/d0c/group__calib3d.html#ga549c2075fac14829ff4a58bc931c033d
	- Issue announced: https://stackoverflow.com/questions/44042323/opencv-error-assertion-failed-in-undistort-cpp-at-line-293
	-Resolved: https://github.com/opencv/opencv/issues/4943

3. SOLVEPNP_P3P 
	Method is based on the paper of X.S. Gao, X.-R. Hou, J. Tang, H.-F. Chang “Complete Solution Classification for the Perspective-Three-Point Problem”. In this case, the function requires exactly four object and image points.

4. SOLVEPNP_EPNP 
	Method has been introduced by F.Moreno-Noguer, V.Lepetit and P.Fua in the paper “EPnP: Efficient Perspective-n-Point Camera Pose Estimation”.


### Listed below are exclusive to OpenCV 3:

NOTE: 
	The following two have been listed as unstable in the OpenCV 3.2 documentation : Refer note in http://docs.opencv.org/3.2.0/d9/d0c/group__calib3d.html#ga549c2075fac14829ff4a58bc931c033d

1. SOLVEPNP_DLS 
	Method is based on the paper of Joel A. Hesch and Stergios I. Roumeliotis. “A Direct Least-Squares (DLS) Method for PnP”.
2. SOLVEPNP_UPNP 
	Method is based on the paper of A.Penate-Sanchez, J.Andrade-Cetto, F.Moreno-Noguer. “Exhaustive Linearization for Robust Camera Pose and Focal Length Estimation”. In this case the function also estimates the parameters f_x and f_y assuming that both have the same value. Then the cameraMatrix is updated with the estimated focal length.
import cv2 as cv
import glob
import numpy as np
 
#Chessboard images
images_folder = '*.jpg'
images_names = sorted(glob.glob(images_folder))
images = []
for imname in images_names:
    im = cv.imread(imname, 1)
    images.append(im)    

#termination criteria
criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 30, 0.001)
 
#find chessboard corners - obj points and image points
rows = 6
columns = 8 
world_scaling = 1. 
 
#coordinates of squares in the checkerboard world space
objp = np.zeros((rows*columns,3), np.float32)
objp[:,:2] = np.mgrid[0:rows,0:columns].T.reshape(-1,2)
objp = world_scaling* objp
 
 
#frame dimensions. Frames should be the same size.
width = images[0].shape[1]
height = images[0].shape[0]
 
#Pixel coordinates of checkerboards
imgpoints = [] # 2d points in image plane.
 
#coordinates of the checkerboard in checkerboard world space.
objpoints = [] # 3d point in real world space
 
 
for frame in images:
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
 
    #find the checkerboard
    ret, corners = cv.findChessboardCorners(gray, (rows, columns), None)
 
    if ret == True:
 
        #Convolution size used to improve corner detection. Don't make this too large.
        conv_size = (11, 11)
 
        #opencv can attempt to improve the checkerboard coordinates
        corners = cv.cornerSubPix(gray, corners, conv_size, (-1, -1), criteria)
        cv.drawChessboardCorners(frame, (rows,columns), corners, ret)
        cv.imshow('img', frame)
        k = cv.waitKey(500)
 
        objpoints.append(objp)
        imgpoints.append(corners)
    
ret, mtx, dist, rvecs, tvecs = cv.calibrateCamera(objpoints, imgpoints, (width, height), None, None)
print("Frame availability:", ret, "\n")
print("Matrix:", mtx, "\n")
print("Camera distortion:",dist, "\n")
print("Output vector of rotation vectors: \n", rvecs, "\n")
print("Output vector of translaton vectors: \n",tvecs)